import time
from . import Helper

mSample=""
mSampleBeginTime=0

def BeginSample(varSample):
    global mSample
    global mSampleBeginTime
    mSample=varSample
    mSampleBeginTime=Helper.GetUnixTimeStamp_ms()

def EndSample():
    global mSampleBeginTime
    tmpCostTime=Helper.GetUnixTimeStamp_ms()-mSampleBeginTime
    print("ProfilerTime "+mSample+":"+str(tmpCostTime))
    return tmpCostTime
