import sys

data = open(sys.argv[-1],"r").read()


h2bc = {"0":"0000",
        "1":"0001",
        "2":"0010",
        "3":"0011",
        "4":"0100",
        "5":"0101",
        "6":"0110",
        "7":"0111",
        "8":"1000",
        "9":"1001",
        "A":"1010",
        "B":"1011",
        "C":"1100",
        "D":"1101",
        "E":"1110",
        "F":"1111",}

a = ""


for i in data:
    a += h2bc[i]

data = a

print(data)

#data = '110100101111111000101000'

def getValue(data):
    print(data)
    V = int(data[:3],2)
    T = int(data[3:6],2)
    c = 0
    l = 6
    d = ''
    if T==4:
        while True:
            a = data[6+5*c:11+5*c]
            d += a[1:]
            if a[0] == '0':
                break
            c+=1
        l += int((len(d)/4)*5)
        d = int(d,2)
        return V,d,l
    else:
        I = int(data[6],2)
        if I == 0:
            tb = int(data[7:22],2)
            l = 22
            cb = 0
            d = 0
            while cb < tb:
                a = getValue(data[22+cb:])
                cb += a[-1]
                d += a[1]
                V += a[0]
            l+=cb
            return V,d,l
        elif I==1:
            tp = int(data[7:18],2)
            l = 18
            cb = 0
            d = 0
            for i in range(tp):
                a = getValue(data[18+cb:])
                cb+= a[-1]
                d += a[1]
                V += a[0]
            l+=cb
            return V,d,l



print(getValue(data))