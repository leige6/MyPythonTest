# coding:utf-8
import os
import sys
import pickle #二进制序列化要引入的包
import json #json序列化要引入的包
from functools import reduce #导入reduce相关类
print '张亚磊'
s='  aaaaa '
print s.strip()
print s.upper()
print s.strip().capitalize()
#位置比较
s_1='abcdefg'
s_2='abcefg'
try:
    print s_1.index('bcd')
    print s_2.index('bcd')
except  ValueError:
    print "值未找到"
print cmp(s_1,s_2)
print s_1 is s_2
print s_1.startswith('abc')
print 'abc'.isalpha() #是否全是字母
print '123231'.isdigit() #是否全是数字
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
#集合用 not XX 判断是否为empty 与is None不是一回事
l_a=[]
if not l_a:
    print 'Empty'
if l_a is None:
    print 'None'
print '-------------------------'
#容器切片练习
li_2a=[i*2 for i in range(10)]
print li_2a
li_2b=[[0]*3 for i in range(3)]
print li_2b
print '-------------------------'
la_a=[]
while la_a:
    print '进入'
else:
    print '未进入'
print '-------------------------'
for i in range(10,1,-1):
    print i
print '------------文件操作os相关方法讲解-------------'
print sys.path 
print os.path.abspath('.') #当前目录的绝对路径
print os.path.join('F:\py','ad') #连接一个路径
print os.path.split('F:/py/a.txt') #将路径拆分成两部分，最后一部分总是文件名
print os.path.splitext('F:/py/a.txt') #可以直接得到文件扩展名
#删除文件   os.remove()  
#重命名文件   os.rename('','') 
print [x for x in os.listdir('.') if os.path.isdir(x)] #列出当前目录下所有目录
print [x for x in os.listdir('.') if os.path.isfile(x)]  #列出当前目录下所有文件
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']  #列出当前目录下所有.py结尾的文件
print '------------二进制序列化相关方法讲解-------------'
#if not os.path.exists('a.txt'):
#    os.mkdir('a.txt') #创建一个存储序列化的文件夹
d=dict(name='思聪',age='26',sex='男')
str=pickle.dumps(d) #调用pickle的dumps函数进行序列化
print str
f=open('a.txt','wb') #  a.txt不存在就创建
pickle.dump(d,f)
f.close()
print '------------二进制反序列化相关方法讲解-------------'
f=open('a.txt','rb')
d=pickle.load(f) #调用load做反序列化操作
f.close()
print d
print 'name is %s' %d['name']
print 'age is %s' %d['age']
print 'sex is %s' %d['sex']
print '------------json序列化相关方法讲解-------------'
d1=dict(name='思聪',age='26',sex='男')
#调用json函数的dumps方法进行序列化dumps方法，可将json格式数据序列为Python的相关的数据类型，通常用于打印等；loads方法则是相反，把python数据类型转换为json#相应的数据类型格式要求，反序列化后可以对json数据进行各种操作。在编程过程还发现一个问题，在序列化时，中文汉字总是被转换为unicode码，在网上搜索后发现，在#dumps函数中添加参数ensure_ascii=False即可解决。
str=json.dumps(d1,ensure_ascii=False) 
print str
d2=json.loads(str,'gb2312')
print d2
print '------------reduce相关方法讲解-------------'
l=[1,2,3,4,5]
print reduce(lambda x,y:x+y,l)
#如果你给x一个初始值放在list后面
print reduce(lambda x,y:x+y,l,10)
print '------------map相关方法讲解-------------'
l1=[1,2,3]
new_list=list(map(lambda i:i+1,l1))
print new_list
#也可把两个list合并成一个list
l2=[3,4,5]
new_list2=list(map(lambda x,y:x+y,l1,l2))
print new_list2
print '------------filter相关方法讲解-------------'
l3=[100,20,24,60,75,80]
la=list(filter(lambda x:x<50,l3)) #过滤输出list中小于50的数
print la




















os.system('pause')
