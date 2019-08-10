
from numba import jit
import time
#@jit
def gezidian():
    fileobj=open('zidian.txt','a',encoding='utf-8')
    list1=[]
    list2=['0','1','2','3','4','5','6','7','8','9','x']
    i=1
    while(i<=31):
        list1.append(str(i).zfill(2))
        
        ii=0
        while(ii<=999):
            
            
            
            iii=0
            while iii<=10:
                fileobj.write(list1[i-1])
                fileobj.write(str(ii).zfill(3))
                fileobj.write(list2[iii])
                fileobj.write('\n')
                iii+=1
            ii+=1
        i+=1
        
    
start = time.time()
gezidian()
end = time.time()
print(end-start)