n11,k11=map(int,input().split())
l=list(map(int,input().split()))
s11=list(map(int,input().split()))
k11=""
for i in s11:
    l.append(i)
    k11=k11+str(max(l))+" "
print(k11.strip())
