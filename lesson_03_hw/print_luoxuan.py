# coding:utf-8
def printStr(list):
    ret=[]
    rows=len(list)
    if rows == 0:
        return ret
    colums=len(list[0])
    i,j=0,0
    while rows>0 and colums>0:
        for k in range(j,j+colums):
            ret.append(list[i][k])  #取第一行的数
        if rows>1:
            for k in range(i+1,i+rows):
                ret.append(list[k][j+colums-1])  #最右列
            if colums>1:
                for k in range(j+colums-2,j,-1):
                    ret.append(list[i+rows-1][k]) #最下行
                for k in range(i+rows-1,i,-1):
                    ret.append(list[k][j]) #最左列
        rows -= 2
        colums -= 2
        i += 1
        j += 1
    return ret

s=printStr([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print s