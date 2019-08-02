x11,y11=map(int,input().split())
x22,y22=map(int,input().split())
x33,y33=map(int,input().split())
if x11==y11 and x22==y22 and x33==y33:
	print("yes")
elif x11==x22 and x11==x33:
	print("yes")
elif y11==y22 and y11==y33:
	print("yes")
else:
	print("no")
