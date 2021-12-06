

data = open("2021d1.txt","r").read().split("\n")





cv = 0

t = 0

for i in data:
	if int(i)>cv:
		t+=1
	cv = int(i)




print(t-1)
