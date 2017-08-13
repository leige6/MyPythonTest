from multiprocessing import Process
import time


def f(n):
    time.sleep(1)
    print n*n

if __name__=='__main__':
    start_time=time.time()
    for i in range(1,10):
        #f(i)
        p=Process(target=f,args=[i,])
        p.start()
    end_time=time.time()
    print "Total time:{}".format(end_time-start_time)