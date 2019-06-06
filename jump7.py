#for i in range(1,101):
#	print (i)
a = 0

while a<100:
	a+=1
	i = str(a).find("7")
	if i==-1 and int(a)%7 !=0:
		print(a)

