
import sys


data = open(sys.argv[-1],"r").read().split("\n")

print(data)

data = data[:-1]


sums = []


for i in range(len(data)-2):
	sums.append((int(data[i])+int(data[i+1])+int(data[i+2])))
	

print(data)

data = sums

print(data)


cv = 0

t = 0

for i in data:
	if int(i)>cv:
		t+=1
	cv = int(i)




print(t-1)
