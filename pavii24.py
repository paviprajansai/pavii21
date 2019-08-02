s11=input()
for i1 in s11:
	if i1.isdigit():
		flag=0
	else:
		flag=1
		break
if flag==0:
	print("yes")
else:
	print("no")
