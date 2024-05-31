n=19
temp=0
res=0
def happynumber(n):
    temp=n
    temp=temp%10
    res+=(temp**2)*10
    n=n//10
    n=temp
print(happynumber(19))
    
    