n11=int(input())
l=list(map(str,input().split()))
p=sorted(l,key=len)
for i1 in range(len(p1)-1):
    if len(p1[i1])==len(p1[i1+1]) and p1[i1]>p1[i1+1]:
        p1[i1],p1[i1+1]=p1[i1+1],p1[i1]
print(*p1)
