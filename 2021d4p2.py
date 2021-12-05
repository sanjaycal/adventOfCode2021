import sys


data = open(sys.argv[-1],"r").read().split('\n\n')



cns = []

for i in data[0].split(','):
    cns.append(int(i))

data = data[1:]

mask = []

for i in range(len(data)):
    mask.append([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])


boards = []

for i in data:
    boardstart = i.split("\n")
    board = []
    for j in boardstart:
        a = j.split(' ')
        b = []
        for k in a:
            if k!='':
                b.append(int(k))
        board.append(b)

    boards.append(board)


def editMask(n,boardn):
    for i in range(5):
        for j in range(5):
            if boards[boardn][i][j]==n:
                mask[boardn][i][j] = 1


def checkRow(boardn):
    for i in range(5):
        count = 0
        for j in range(5):
            count+=mask[boardn][i][j]
        if count == 5:
            return True
    return False


def checkCol(boardn):
    for i in range(5):
        count = 0
        for j in range(5):
            count+=mask[boardn][j][i]
        if count == 5:
            return True
    return False


def getScore(boardn):
    score = 0
    for i in range(5):
        for j in range(5):
            if mask[boardn][i][j] == 0:
                score+=boards[boardn][i][j]
    return score

def main():
    for i in cns:
        print(len(boards))
        if len(boards)>0:
            count = 0
            for j in range(len(boards)):
                
                editMask(i,j-count)
                if checkRow(j-count) or checkCol(j-count):
                    if len(boards)==1:
                        return(getScore(0)*i)
                    boards.pop(j-count)
                    mask.pop(j-count)
                    count+=1
        else:
            return getScore(0)




print(main())