import time

def showTime(time=time.ctime()):
    print(time)

showTime(time.ctime())
time.sleep(5)
showTime(time.ctime())
time.sleep(5)
showTime(time.ctime())
