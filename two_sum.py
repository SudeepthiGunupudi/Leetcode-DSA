a=[]
n = int(input())
for l in range(0, n):
    ele = int(input())
    # adding the element
    a.append(ele)  
t=int(input())
for i in a:
    for j in a:
        if i==j:
            break
        else:
            k=i+j
            if t==k:
                print('i['+str(a.index(i))+']='+str(i),'i['+str(a.index(j))+']='+str(j)+'  sum='+str(t))