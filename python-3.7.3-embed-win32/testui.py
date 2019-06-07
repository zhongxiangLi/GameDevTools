import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from testDialog import Ui_Dialog


class Test_Form(QDialog):

    #构造函数,创建一个新的Dialog
    #制作的界面是Dialog，但是生成的代码里面是没有创建Dialog的，只有Dialog上面其他控件的代码，所以要创建一个Dialog
    def __new__(cls,*args,**kwargs):
        return QDialog.__new__(cls,*args,**kwargs)

    def __init__(self,*args,**kwargs):#先执行构造函数，然后执行初始化函数
        QDialog.__init__(self,*args,**kwargs)
        self.ui= Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    # 所有应用必须创建一个应用（Application）对象
    app = QApplication(sys.argv)
    form = Test_Form()
    form.show()
    sys.exit(app.exec_())