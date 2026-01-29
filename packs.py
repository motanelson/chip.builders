def packs(s):
    num=[256*256*256,256*256,256,1]
    remain=c
    bbbb=""
    for n in range(3):
       i:int=remain//num[n]
       ii=i*num[n]
       bbb:chr=chr(i)
       remain=remain-ii
       bbbb=bbb+bbbb
    bbbb=chr(remain)+bbbb
    return bbbb.encode()
print( "\033c\033[40;37m\n ? ")
a="my.dat"
b=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
f1=open(a,"wb")
for c in b:
    
    f1.write(packs(c))
f1.close()
