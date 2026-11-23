import threading as th
import time
def Square(num1):
    print("Thread 1 started")
    sq = num1*num1
    time.sleep(5)
    print(sq)
    
def Cube(num1):
    print("thread 2 started")
    cu = num1* num1 * num1
    print(cu)

t1 = th.Thread(target=Square, args=[3,])
t2 = th.Thread(target=Cube, args=(6, ))

t1.start()
t2.start()


#print(t1.getname())