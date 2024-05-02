x=[-1,0,1,2,-1,-4]
x.sort()
l=0
r=len(x)-1
while l<r:
    current=x[l]+x[r]
    if(current)>0:
        r-=1
    elif(current<0):
        l+=1
    else:
        print(x[l],x[r])
        break