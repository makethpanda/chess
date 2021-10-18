class Piece:
    def show(self):
        return str(self.p)+str(self.color)
    def __init__(self,color,piece,y,x):
        self.color = color
        self.p = piece
        self.y = y
        self.x = x
    def move(self,x,y,check):
        if (y,x) in check:
            listplace(y,x,internalboard[self.y][self.x])
            listplace(self.y,self.x,"__")
            self.y = y
            self.x = x
        else:
            print("invalid move")
class Rook(Piece):
    def __init__(self, color, piece,y,x):
        super().__init__(color, piece,y,x) 
    def getmoverange(self):
        moverange = []
        x = self.x+1 
        y = self.y
        
        while x<=7:
            if board[y][x]!="__" and board[y][x][1]!=self.color:
                
                moverange.append((y,x))
                break
            elif board[y][x][1]==self.color:
                break
            else:
                moverange.append((y,x))         
            x+=1
        x = self.x-1
        while x>=0:
            if board[y][x]!="__" and board[y][x][1]!=self.color:
                moverange.append((y,x))
                break
            elif board[y][x][1]==self.color:
                break
            else:
                moverange.append((y,x))         
            x-=1
        x = self.x
        y = self.y+1
        while y<=7:
            if board[y][x]!="__" and board[y][x][1]!=self.color:
                
                moverange.append((y,x))
                break
            elif board[y][x][1]==self.color:
                break
            else:
                moverange.append((y,x))         
            y+=1
        y = self.y-1
        while y>=0:
            if board[y][x]!="__" and board[y][x][1]!=self.color:
                moverange.append((y,x))
                break
            elif board[y][x][1]==self.color:
                break
            else:
                moverange.append((y,x))         
            y-=1   
        return moverange
class Pawn(Piece):
    def basepos(self):
        if self.color=="b":
            return 6
        else:return 1
    def __init__(self, color, piece,y,x):
        super().__init__(color, piece,y,x) 
        if self.color =="b":
            self.advancement = -1
        else:
            self.advancement = 1
    def getmoverange(self):
        moverange = []
        if isempty(board,self.y+self.advancement,self.x):
            moverange.append((self.y+self.advancement,self.x))
        if self.y == self.basepos():
            if isempty(board,self.y+2*self.advancement,self.x) and isempty(board,self.y+self.advancement,self.x):
                moverange.append((self.y+2*self.advancement,self.x))
        if self.x<7:
            if not isempty(board,self.y+self.advancement,self.x+1):
                if self.color != checkboard(board,self.y+self.advancement,self.x+1):
                    moverange.append((self.y+self.advancement,self.x+1))
        if 0<self.x:
            if not isempty(board,self.y+self.advancement,self.x-1):
                if self.color != checkboard(board,self.y+self.advancement,self.x-1):
                    moverange.append((self.y+self.advancement,self.x-1))
        return moverange
class Knight(Piece):
    def __init__(self, color, piece,y,x):
        super().__init__(color, piece,y,x) 
    def getmoverange(self):
        moverange = []
        y = self.y
        x = self.x
        movelist = []
        if x-2>-1 and y+1<8:
            movelist.append((x-2,y+1))
        if x-2>-1 and y-1>-1:
            movelist.append((x-2,y-1))
        if x+2<8 and y+1<8:
            movelist.append((x+2,y+1))
        if x+2<8 and y-1>-1:
            movelist.append((x+2,y-1))
        if x-1>-1 and y+2<8:
            movelist.append((x-1,y+2))
        if x-1>-1 and y-2>-1:
            movelist.append((x-1,y-2))
        if x+1<8 and y+2<8:
            movelist.append((x+1,y+2))
        if x+1<8 and y-2>-1:
            movelist.append((x+1,y-2))
        for i in movelist:
            if board[i[1]][i[0]]!="__" and board[i[1]][i[0]][1]!=self.color:
                moverange.append((i[1],i[0]))
            elif board[i[1]][i[0]][1]==self.color:
                pass
            else:
                moverange.append((i[1],i[0]))
        return moverange
class Bishop(Piece):
    def __init__(self, color, piece,y,x):
        super().__init__(color, piece,y,x) 
    def getmoverange(self):
        moverange = []
        x = self.x
        y = self.y
        #x+ y+
        while x+1<8 and y+1<8:
            x = x+1
            y =y+1
            if board[y][x]!="__" and board[y][x][1]!=self.color:
                moverange.append((y,x))
                break
            elif board[y][x][1]==self.color:
                break
            else:
                moverange.append((y,x))         
            x+=1
            y+=1
        #x- y+
        while x-1>-1 and y+1<8:
            x = x-1
            y =y+1
            if board[y][x]!="__" and board[y][x][1]!=self.color:
                moverange.append((y,x))
                break
            elif board[y][x][1]==self.color:
                break
            else:
                moverange.append((y,x))         
            x+=-1
            y+=1
        #x+ y-
        while x+1<8 and y-1<8:
            x = x+1
            y =y+1
            if board[y][x]!="__" and board[y][x][1]!=self.color:
                moverange.append((y,x))
                break
            elif board[y][x][1]==self.color:
                break
            else:
                moverange.append((y,x))         
            x+=1
            y+=-1
        #x- y-
        while x-1>-1 and y-1>-1:
            x = x+1
            y =y+1
            if board[y][x]!="__" and board[y][x][1]!=self.color:
                moverange.append((y,x))
                break
            elif board[y][x][1]==self.color:
                break
            else:
                moverange.append((y,x))         
            x+=1
            y+=-1
        
        return moverange
#setup vars---------------------------------------------------------
internalboard =  [ ["__" for i in range(8)] for _ in range(8) ]
board = [ ["__" for i in range(8)] for _ in range(8) ]
length = ["a","b","c","d","e","f","g","h"]
height = ["1","2","3","4","5","6","7","8"]
tiles = [[length[i]+height[j]for i in range(8)] for j in range(8)]
movement = -1
posb = 5
def listplace(y,x,item):
    internalboard[y][x]=item
    if item != "__":
        board[y][x]=item.show()
    else:
        board[y][x]="__"
def isempty(board,y,x):
    if board[y][x]=="__" and -1< x < 8 and -1< y < 8:
        return True
    else: 
        return False
def checkboard(board,y,x):
    return board[y][x]
def show(b):
    for i in b:
        print()
        print(i)
for i in range(len(board[0])):
    listplace(1,i,Pawn("w","p",1,i))
    listplace(6,i,Pawn("b","p",6,i))
listplace(0,0,Rook("w","r",0,0))
listplace(0,7,Rook("w","r",0,7))
listplace(7,0,Rook("b","r",7,0))
listplace(7,7,Rook("b","r",7,7))
listplace(4,4,Knight("b","k",4,4))
#-----------------------------------------------------------------
while True:
    
    x = input("nextmove: ")#ex:e2e4
    indexofthing = (length.index(x[0]),height.index(x[1]))
    indexofmove = (length.index(x[2]),height.index(x[3]))
    mover = internalboard[indexofthing[1]][indexofthing[0]]
    mover.move(indexofmove[0],indexofmove[1],mover.getmoverange())
    show(board)