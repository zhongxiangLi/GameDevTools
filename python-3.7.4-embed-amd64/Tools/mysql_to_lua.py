import os
import sys
from . import Helper
import pymysql


def ShowReadme():
        Helper.ShowReadme("导出Mysql 表数据为 lua数据")

TypeNumber=["TINYINT","SMALLINT","MEDIUMINT","INT","INTEGER","BIGINT","FLOAT","DOUBLE","DECIMAL"]
TypeNumber_Lower=[]
for tmpType in TypeNumber:
        TypeNumber_Lower.append(tmpType.lower())
def isNumber(varTypeName):
        if (varTypeName in TypeNumber) or (varTypeName in TypeNumber_Lower):
                return True
        return False
        
# varUsePrimaryKey:是否使用主键，生成字典形式Table
def Export_Mysql_to_Lua(varIP,varUser,varPasswd,varDBName,varSaveDirPath,varPort=3306,varUsePrimaryKey=False):
        
        # 打开数据库连接
        """
        arguments:

        :param host: Host where the database server is located
        :param user: Username to log in as
        :param password: Password to use.
        :param database: Database to use, None to not use a particular one.
        :param port: MySQL port to use, default is usually OK. (default: 3306)
        :param bind_address: When the client has multiple network interfaces, specify
                the interface from which to connect to the host. Argument can be
                a hostname or an IP address.
        :param unix_socket: Optionally, you can use a unix socket rather than TCP/IP.
        :param read_timeout: The timeout for reading from the connection in seconds (default: None - no timeout)
        :param write_timeout: The timeout for writing to the connection in seconds (default: None - no timeout)
        :param charset: Charset you want to use.
        :param sql_mode: Default SQL_MODE to use.
        :param read_default_file:
                Specifies  my.cnf file to read these parameters from under the [client] section.
        :param conv:
                Conversion dictionary to use instead of the default one.
                This is used to provide custom marshalling and unmarshaling of types.
                See converters.
        :param use_unicode:
                Whether or not to default to unicode strings.
                This option defaults to true for Py3k.
        :param client_flag: Custom flags to send to MySQL. Find potential values in constants.CLIENT.
        :param cursorclass: Custom cursor class to use.
        :param init_command: Initial SQL statement to run when connection is established.
        :param connect_timeout: Timeout before throwing an exception when connecting.
                (default: 10, min: 1, max: 31536000)
        :param ssl:
                A dict of arguments similar to mysql_ssl_set()'s parameters.
        :param read_default_group: Group to read from in the configuration file.
        :param compress: Not supported
        :param named_pipe: Not supported
        :param autocommit: Autocommit mode. None means use server default. (default: False)
        :param local_infile: Boolean to enable the use of LOAD DATA LOCAL command. (default: False)
        :param max_allowed_packet: Max size of packet sent to server in bytes. (default: 16MB)
                Only used to limit size of "LOAD LOCAL INFILE" data packet smaller than default (16KB).
        :param defer_connect: Don't explicitly connect on contruction - wait for connect call.
                (default: False)
        :param auth_plugin_map: A dict of plugin names to a class that processes that plugin.
                The class will take the Connection object as the argument to the constructor.
                The class needs an authenticate method taking an authentication packet as
                an argument.  For the dialog plugin, a prompt(echo, prompt) method can be used
                (if no authenticate method) for returning a string from the user. (experimental)
        :param server_public_key: SHA256 authenticaiton plugin public key value. (default: None)
        :param db: Alias for database. (for compatibility to MySQLdb)
        :param passwd: Alias for password. (for compatibility to MySQLdb)
        :param binary_prefix: Add _binary prefix on bytes and bytearray. (default: False)
        """
        db = pymysql.connect(varIP,varUser,varPasswd,varDBName,varPort)
        
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        
        #BEGIN 查询版本
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("SELECT VERSION()")
        
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        
        print ("Database version : %s " % data)
        #END

        #BEGIN 获取所有表名
        cursor.execute("SHOW TABLES")
        tmpTableNameList = cursor.fetchall()
        # print(tmpTableNameList)
        #END

        #BEGIN 导出
        for tmpTableName in tmpTableNameList:
                tmpTableName=tmpTableName[0]
                print(u"导出>" + tmpTableName)
                # cursor.execute("select * from "+tmpTableName)
                # tmpTableData=cursor.fetchall()
                # print(tmpTableData)

                #获取字段名，字段注释，字段类型
                cursor.execute("select column_name,column_comment,data_type from information_schema.COLUMNS where table_name = '"+tmpTableName+"' and table_schema = '"+varDBName+"';")
                tmpTableColumnInfos=cursor.fetchall()
                print(tmpTableColumnInfos)

                #获取主键
                cursor.execute("SELECT column_name FROM INFORMATION_SCHEMA.`KEY_COLUMN_USAGE` WHERE table_name='"+tmpTableName+"' AND constraint_name='PRIMARY'")
                tmpTableColumnPrimary=cursor.fetchone()
                if tmpTableColumnPrimary==None:
                        print(u"没有设置主键")
                else:
                        tmpTableColumnPrimary=tmpTableColumnPrimary[0]
                        print(u"主键>"+tmpTableColumnPrimary)

                #查询数据
                tmpQueryStr="select "
                for tmpTableColumnInfo in tmpTableColumnInfos:
                        tmpTableColumnName=tmpTableColumnInfo[0]
                        tmpQueryStr=tmpQueryStr+"`"+tmpTableColumnName+"`,"
                tmpQueryStr=tmpQueryStr[0:-1]
                tmpQueryStr=tmpQueryStr+" from "+tmpTableName
                # print(tmpQueryStr)
                cursor.execute(tmpQueryStr)
                tmpTableData=cursor.fetchall()
                # print(tmpTableData)

                #生成lua
                tmpTableLuaStr=tmpTableName+"=\n{\n"

                for tmpRowData in tmpTableData:
                        tmpTableColumnDataPrimary=None
                        tmpRowLuaStr="{"
                        for tmpColumnIndex in range(len(tmpTableColumnInfos)):
                                tmpColumnName=tmpTableColumnInfos[tmpColumnIndex][0]
                                tmpColumnType=tmpTableColumnInfos[tmpColumnIndex][2]

                                tmpColumnData=tmpRowData[tmpColumnIndex]
                                if tmpColumnName==tmpTableColumnPrimary:
                                        tmpTableColumnDataPrimary=tmpColumnData

                                # print("tmpColumnName="+tmpColumnName)
                                # print(tmpColumnData)
                                if isNumber(tmpColumnType):
                                        if tmpColumnData==None:
                                                tmpColumnData=0
                                        tmpRowLuaStr=tmpRowLuaStr+tmpColumnName+"="+str(tmpColumnData)+","
                                else:
                                        if tmpColumnData==None:
                                                tmpColumnData=""
                                        #字符串内容 对引号进行处理
                                        tmpColumnData=tmpColumnData.replace("'","\\'")
                                        tmpColumnData=tmpColumnData.replace('"','\\"')
                                        tmpRowLuaStr=tmpRowLuaStr+tmpColumnName+"='"+tmpColumnData+"',"
                                        
                        tmpRowLuaStr=tmpRowLuaStr[0:-1]+"},\n"

                        #有主键，则作为字典形式存储
                        if tmpTableColumnDataPrimary==None or varUsePrimaryKey==False:
                                tmpRowLuaStr="    "+tmpRowLuaStr
                        else:
                                tmpRowLuaStr="    ["+str(tmpTableColumnDataPrimary)+"]="+tmpRowLuaStr

                        tmpTableLuaStr=tmpTableLuaStr+tmpRowLuaStr
                tmpTableLuaStr=tmpTableLuaStr+"}\n"
                # print(tmpTableLuaStr)
                Helper.WriteStrToTxtFile(tmpTableLuaStr,varSaveDirPath+"/"+tmpTableName+".lua")
                # break
        #END
        
        # 关闭数据库连接
        db.close()

def run():
        ShowReadme()

        tmpUseConfig=1#是否使用上次的配置,默认使用
        tmpConfig={}
        tmpConfigJsonFilePath=Helper.GetSystemAppDataDirPath()+"mysql_to_lua.config.json"
        if os.path.exists(tmpConfigJsonFilePath) and os.path.isfile(tmpConfigJsonFilePath):
                tmpconfigJson=Helper.ReadTxtFileToStr(tmpConfigJsonFilePath)
                print(u"检测到上次配置\n"+tmpconfigJson+"\n")
                
                tmpUseConfig=1
                tmpUseConfig=Helper.String_to_int(input(u"是否使用上次的配置,否输入0 (默认1):"),1)
                if tmpUseConfig==1:
                        tmpConfig=eval(tmpconfigJson)
        else:
                tmpUseConfig=0
        
        if tmpUseConfig==0:

                tmpIP=""
                while tmpIP=="":
                        tmpIP=input(u"输入Mysql IP(127.0.0.1):")
                        tmpIP=Helper.Remove_r_n(tmpIP)

                

                tmpUser=""
                while tmpUser=="":
                        tmpUser=input(u"输入账号:")
                        tmpUser=Helper.Remove_r_n(tmpUser)

                tmpPasswd=""
                while tmpPasswd=="":
                        tmpPasswd=input(u"输入密码:")
                        tmpPasswd=Helper.Remove_r_n(tmpPasswd)

                tmpDBName=""
                while tmpDBName=="":
                        tmpDBName=input(u"输入数据库名字:")
                        tmpDBName=Helper.Remove_r_n(tmpDBName)

                tmpSaveDirPath=""
                while tmpSaveDirPath=="":
                        tmpSaveDirPath=input(u"输入lua存放目录:")
                        tmpSaveDirPath=Helper.Remove_r_n(tmpSaveDirPath)
                        tmpSaveDirPath=Helper.getUnixPath(tmpSaveDirPath)
                        if os.path.isdir(tmpSaveDirPath)==False:
                                print(u"目录不对")
                                tmpSaveDirPath=""

                tmpPort=3306
                tmpPort=Helper.String_to_int(input(u"输入端口(默认3306):"),3306)

                tmpUsePrimaryKey=0
                tmpUsePrimaryKey=Helper.String_to_int(input(u"是否根据主键，生成字典形式Table,确认输入1 (默认0):"),0)


                if tmpUsePrimaryKey==1:
                        tmpUsePrimaryKey=True
                else:
                        tmpUsePrimaryKey=False


                #写入配置文件
                tmpConfig["IP"]=tmpIP
                tmpConfig["User"]=tmpUser
                tmpConfig["Passwd"]=tmpPasswd
                tmpConfig["DBName"]=tmpDBName
                tmpConfig["SaveDirPath"]=tmpSaveDirPath
                tmpConfig["Port"]=tmpPort
                tmpConfig["UsePrimaryKey"]=tmpUsePrimaryKey
                tmpConfigJson=str(tmpConfig)
                Helper.WriteStrToTxtFile(tmpConfigJson,Helper.GetSystemAppDataDirPath()+"mysql_to_lua.config.json")

        
        Export_Mysql_to_Lua(tmpConfig["IP"],tmpConfig["User"],tmpConfig["Passwd"],tmpConfig["DBName"],tmpConfig["SaveDirPath"],tmpConfig["Port"],tmpConfig["UsePrimaryKey"])

                
        
        
        
        

if __name__=="__main__":
    run()
