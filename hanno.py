# coding:utf-8
import os
from math import sqrt
print '------------------'
#�ַ�����ת
print '�ַ�����ת'
str_a='I love china!'
list_str=str_a.split(' ')
list_revise_str=list(reversed(list_str))
result_str=' '.join(list_revise_str)
print result_str
print '------------------'
#��ŵ������
print '��ŵ������'
def hanno(n,A,B,C):
    if n==1:
	    print A+'->'+B
    else:
        hanno(n-1,A,C,B)
        print A+'->'+B
        hanno(n-1,C,B,A)
		
hanno(4,'A','B','C')
print '------------------'
#��n���ڵ�����
print '��n���ڵ�����'
def prime(n):
    number=[]
    for i in xrange(2,n,1):
        for j in xrange(2,int(sqrt(i)),1):
            if i%j==0:
                break
        else:
            number.append(i)
    
    return number

while True:
    num=raw_input("��������Ҫ���������Χ:")
    if not num.isdigit():
        print '������һ���Ϸ������֣�'
    else:
        num=int(num)
        break    
ans=prime(num)
print len(ans)
print ans
print '------------------'
    
    
    

os.system('pause')