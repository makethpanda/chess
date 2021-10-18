import random
length = ["a","b","c","d","e","f","g","h"]
height = ["1","2","3","4","5","6","7","8"]
tiles = [[length[i]+height[j]for i in range(8)] for j in range(8)]
board = empty_lists = [ ["__" for i in range(8)] for _ in range(8) ]
itemboard = empty_lists = [ ["__" for i in range(8)] for _ in range(8) ]
def getpos(x):
    return tiles.index(x)
def showboard(b):
    for i in b:
        print(i)
class Piece:
    class Rook:
        def __init__(self,color,pos):
            self.color = color
            if self.color == "B":#black
                self.column = pos
                self.advancement = 6
            else:
                self.column = pos
                self.advancement = 1
        def show(self):
            return "P"

    class Pawn:
        def __init__(self,color,posx,posy):
            self.color = color
            if self.color == "B":#black
                self.column = posx
                if posy == -1:
                    self.advancement = 6
                else:
                    self.advancement=posy
            else:
                self.column = posx
                self.advancement = 1
        def show(self):
            if self.color =="B":
                return "Pb"
            else:
                return"Pw"
        def canmove(self,amount,board):
            if self.color == "B":
                if amount==2:
                    assert self.advancement==2,"invalid move"
                for i in range(amount):
                    i = i+1
                    assert board[self.advancement-i][self.column]=="_","no empty space"
                self.advancement -= i
                return True
                
        def caneat(self):
            if  self.color == "B":
                if self.column+1 > 7:
                    return ([self.column-1],[self.advancement-1])
                elif self.column-1 <0:
                    return ([self.column+1],[self.advancement-1])
                else:
                    return ([self.column-1],[self.advancement-1]),([self.column+1],[self.advancement-1])
            elif  self.color == "W":
                if self.column+1 > 7:
                    return ([self.column-1],[self.advancement+1])
                elif self.column-1 <0:
                    return ([self.column+1],[self.advancement+1])
                else:
                    return ([self.column-1],[self.advancement+1]),([self.column+1],[self.advancement+1])
    def __init__(self, ptype, color, posx,posy=-1):
        self.color = color
        if ptype == "P":
            self.piece = self.Pawn(color,posx,posy)
    def __str__(self):
            return self.piece
    def move(self, toy, tox, board):
        if board[toy][tox] 
        board[toy][tox] = self.piece.show()
        board[self.piece.advancement][self.piece.column] = "__"
        self.piece.advancement = toy
        self.piece.column = tox
    def place(self, board):
        board[self.piece.advancement][self.piece.column]=self.piece.show()

            
showboard(board)
p1 = Piece("P","B",0)
p2 = Piece("P","B",0,5)
p1.place(board)
p2.place(board)
showboard(board)
p1.move(5,0,board)
showboard(board)