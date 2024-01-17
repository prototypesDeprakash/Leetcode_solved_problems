x=121
x=str(x)
main=[]
for i in x:
    main.append(i)
print(main)

orig =""
revo=""
for i in main:
    orig+=i
print(orig)

for j in range(len(main)-1, 0 if main[0] == '-' else -1, -1):
 
    revo += main[j]

if("-" in main):
    revo+="-"
print(revo)

if(orig==revo):
    print("ture")
else:
    print("false")