from multiprocessing import Process,Queue
import time

def write(q):
    for i in ['A','B','C','D','E']:
        print "put %s to Queue" %i
        q.put(i)
        time.sleep(0.5)
def read(q):
    while True:
        v=q.get(True)
        print "get %s from Queue" %v


if __name__=='__main__':
    q=Queue()
    pw=Process(target=write,args=[q,])
    pr=Process(target=read,args=[q,])
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    pw.terminate()
    pr.terminate()