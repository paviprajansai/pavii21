n11,k11=map(int,input().split())
s11=max(n11,k11)
for i in range(1,s11):
	if n11%i==0 and k11%i==0:
		a=i
if n11==1 and k11==1:
    a=1
print(a)
