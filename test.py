# coding:utf-8
import os
import sys
import pickle #���������л�Ҫ����İ�
import json #json���л�Ҫ����İ�
from functools import reduce #����reduce�����
print '������'
s='  aaaaa '
print s.strip()
print s.upper()
print s.strip().capitalize()
#λ�ñȽ�
s_1='abcdefg'
s_2='abcefg'
try:
    print s_1.index('bcd')
    print s_2.index('bcd')
except  ValueError:
    print "ֵδ�ҵ�"
print cmp(s_1,s_2)
print s_1 is s_2
print s_1.startswith('abc')
print 'abc'.isalpha() #�Ƿ�ȫ����ĸ
print '123231'.isdigit() #�Ƿ�ȫ������
print '-------------------------'
print int('12313')
print float('12.45')
#print int('12.45')
print '-------------------------'
s='abcd'
a=list(s)
print a
print '-------------------------'
for i in range(1,10,2):
    print i
print '-------------------------'
#������ not XX �ж��Ƿ�Ϊempty ��is None����һ����
l_a=[]
if not l_a:
    print 'Empty'
if l_a is None:
    print 'None'
print '-------------------------'
#������Ƭ��ϰ
li_2a=[i*2 for i in range(10)]
print li_2a
li_2b=[[0]*3 for i in range(3)]
print li_2b
print '-------------------------'
la_a=[]
while la_a:
    print '����'
else:
    print 'δ����'
print '-------------------------'
for i in range(10,1,-1):
    print i
print '------------�ļ�����os��ط�������-------------'
print sys.path 
print os.path.abspath('.') #��ǰĿ¼�ľ���·��
print os.path.join('F:\py','ad') #����һ��·��
print os.path.split('F:/py/a.txt') #��·����ֳ������֣����һ���������ļ���
print os.path.splitext('F:/py/a.txt') #����ֱ�ӵõ��ļ���չ��
#ɾ���ļ�   os.remove()  
#�������ļ�   os.rename('','') 
print [x for x in os.listdir('.') if os.path.isdir(x)] #�г���ǰĿ¼������Ŀ¼
print [x for x in os.listdir('.') if os.path.isfile(x)]  #�г���ǰĿ¼�������ļ�
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']  #�г���ǰĿ¼������.py��β���ļ�
print '------------���������л���ط�������-------------'
#if not os.path.exists('a.txt'):
#    os.mkdir('a.txt') #����һ���洢���л����ļ���
d=dict(name='˼��',age='26',sex='��')
str=pickle.dumps(d) #����pickle��dumps�����������л�
print str
f=open('a.txt','wb') #  a.txt�����ھʹ���
pickle.dump(d,f)
f.close()
print '------------�����Ʒ����л���ط�������-------------'
f=open('a.txt','rb')
d=pickle.load(f) #����load�������л�����
f.close()
print d
print 'name is %s' %d['name']
print 'age is %s' %d['age']
print 'sex is %s' %d['sex']
print '------------json���л���ط�������-------------'
d1=dict(name='˼��',age='26',sex='��')
#����json������dumps�����������л�dumps�������ɽ�json��ʽ��������ΪPython����ص��������ͣ�ͨ�����ڴ�ӡ�ȣ�loads���������෴����python��������ת��Ϊjson#��Ӧ���������͸�ʽҪ�󣬷����л�����Զ�json���ݽ��и��ֲ������ڱ�̹��̻�����һ�����⣬�����л�ʱ�����ĺ������Ǳ�ת��Ϊunicode�룬�������������֣���#dumps��������Ӳ���ensure_ascii=False���ɽ����
str=json.dumps(d1,ensure_ascii=False) 
print str
d2=json.loads(str,'gb2312')
print d2
print '------------reduce��ط�������-------------'
l=[1,2,3,4,5]
print reduce(lambda x,y:x+y,l)
#������xһ����ʼֵ����list����
print reduce(lambda x,y:x+y,l,10)
print '------------map��ط�������-------------'
l1=[1,2,3]
new_list=list(map(lambda i:i+1,l1))
print new_list
#Ҳ�ɰ�����list�ϲ���һ��list
l2=[3,4,5]
new_list2=list(map(lambda x,y:x+y,l1,l2))
print new_list2
print '------------filter��ط�������-------------'
l3=[100,20,24,60,75,80]
la=list(filter(lambda x:x<50,l3)) #�������list��С��50����
print la




















os.system('pause')
