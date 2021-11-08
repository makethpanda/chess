from tkinter.constants import W#apparu après l'import 

class Piece:#classe mère pièce
    def show(self):#montrer la pièce sur l'échequier externe
        return str(self.p)+str(self.color)
    def __init__(self,color,piece,y,x):
        self.color = color
        self.p = piece
        self.y = y
        self.x = x
    def move(self,x,y,check):#déplacer une pièce sur une case autorisée
        if (y,x) in check:
            listplace(y,x,internalboard[self.y][self.x])
            listplace(self.y,self.x,"__")
            self.y = y
            self.x = x
        else:
            print("invalid move")
        return 
    def showcolor(self):#renvoie la couleur de la pièce
        return self.color
class Rook(Piece):#classe fille tour 
    def __init__(self, color, piece,y,x):#init de base (voir pion)
        super().__init__(color, piece,y,x) 
    def getmoverange(self):#les mouvments possibles de la tour
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
    def basepos(self):#on établis la positions initialle du pion pour savoir il peut se déplacer de combien
        if self.color=="b":
            return 6
        else:return 1
    def __init__(self, color, piece,y,x):#init, on prends en considération sa position et sa couleur, son type
        super().__init__(color, piece,y,x) 
        if self.color =="b":
            self.advancement = -1
        else:
            self.advancement = 1
    def getmoverange(self):#moverange du pion, dépends de multiples facteurs, renvoie une liste des positions possibles en tuples 
        moverange = []
        if isempty(board,self.y+self.advancement,self.x):#avancer de 1
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
    def geteatrange(self):#les endroits ou le pion peut manger une pièce
        eatrange = []
        if self.x<7:
            if self.color != checkboard(board,self.y+self.advancement,self.x+1):
                eatrange.append((self.y+self.advancement,self.x+1))
        if 0<self.x:
            if self.color != checkboard(board,self.y+self.advancement,self.x-1):
                eatrange.append((self.y+self.advancement,self.x-1))
        return eatrange
class Knight(Piece):#cavalier
    def __init__(self, color, piece,y,x):
        super().__init__(color, piece,y,x) 
    def getmoverange(self):#moverange standart, voir pion
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
class Bishop(Piece):#fou
    def __init__(self, color, piece,y,x):
        super().__init__(color, piece,y,x) 
    def getmoverange(self):#voir pion
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
        x = self.x
        y = self.y
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
        x = self.x
        y = self.y 
        #x+ y-
        while x+1<8 and y-1>-1:
            x = x+1
            y =y-1
            if board[y][x]!="__" and board[y][x][1]!=self.color:
                moverange.append((y,x))
                break
            elif board[y][x][1]==self.color:
                break
            else:
                moverange.append((y,x))   
        x = self.x
        y = self.y       
        #x- y-
        while x-1>-1 and y-1>-1:
            x = x-1
            y =y-1
            if board[y][x]!="__" and board[y][x][1]!=self.color:
                moverange.append((y,x))
                break
            elif board[y][x][1]==self.color:
                break
            else:
                moverange.append((y,x))         
        return moverange
class Queen(Piece):#reine
    def __init__(self, color, piece,y,x):
        super().__init__(color, piece,y,x) 
    def getmoverange(self):#le moverange ici est intelligent: on cherche le moverange d'un fou et d'une tour à la meme place que la dame, économie de code
        moverange = []
        x = self.x
        y = self.y
        moverange = Bishop(self.color,"B",y,x).getmoverange()+Rook(self.color,"R",y,x).getmoverange()
        return moverange
class King(Piece):#roi
    def __init__(self, color, piece,y,x):
        super().__init__(color, piece,y,x) 
    def getmoverange(self):#le roi ne peut que se déplacer si il ne se met pas en echec, donc on utilise possiblemoves pour les coups "possibles " et moverange pour les coupls légaux
        moverange = []
        x = self.x
        y = self.y
        possiblemoves = []
        if x-1>-1:
            possiblemoves.append((y,x-1))
            if y-1>-1:
                possiblemoves.append((y-1,x-1))
            if y+1<8:
                possiblemoves.append((y+1,x-1))
        if y-1>-1:
            possiblemoves.append((y-1,x))
        if x+1<8:
            possiblemoves.append((y,x+1))
            if y-1>-1:
                possiblemoves.append((y-1,x+1))
            if y+1<8:
                possiblemoves.append((y+1,x+1))
        if y+1<8:
            possiblemoves.append((y+1,x))
        for k in possiblemoves:
            moverange.append(k)
        for ligne in internalboard:
                for p in ligne:
                    if p != "__" and p.color != self.color and p.p != "p":
                        for k in moverange:
                            if k in p.getmoverange():
                                moverange.remove(k)
                    elif p != "__" and p.color != self.color and p.p =="p":
                        for k in moverange:
                            if k in p.geteatrange():
                                print(k)
                                moverange.remove(k)
        return moverange
#setup vars---------------------------------------------------------
internalboard =  [ ["__" for i in range(8)] for _ in range(8) ]
board = [ ["__" for i in range(8)] for _ in range(8) ]
length = ["a","b","c","d","e","f","g","h"]
height = ["1","2","3","4","5","6","7","8"]
tiles = [[length[i]+height[j]for i in range(8)] for j in range(8)]
def kingisdead():#test de fin de partie
    global board
    x = 0
    for i in board:
        for j in i:
            if j == "Kb" or  j =="Kw":
                x += 1
    if x ==2:
        return False
    else: return True
def listplace(y,x,item):#placer un élément dans les 2 listes en meme temps
    internalboard[y][x]=item
    if item != "__":
        board[y][x]=item.show()
    else:
        board[y][x]="__"
def isempty(board,y,x):#vérifier si une case est vide
    if board[y][x]=="__" and -1< x < 8 and -1< y < 8:
        return True
    else: 
        return False
def checkboard(board,y,x):#vérifier une position, utile pour connaitre la couleur de l'enemi
    return board[y][x]
def show(b):#show, imprimer chaque ligne de l'échequier ligne par ligne, pour faire joli
    for i in b:
        print()
        print(i)
def getboard():
    return board

def setuppieces():#placer toutes les pièces au bon endroit, soit pour démarer soit pour reccomencer une partie
    global internalboard
    global board
    global turn
    turn = 0
    internalboard =  [ ["__" for i in range(8)] for _ in range(8) ]
    board = [ ["__" for i in range(8)] for _ in range(8) ]
    for i in range(len(board[0])):
        listplace(1,i,Pawn("w","p",1,i))
        listplace(6,i,Pawn("b","p",6,i))
    listplace(0,0,Rook("w","R",0,0))
    listplace(0,7,Rook("w","R",0,7))
    listplace(7,0,Rook("b","R",7,0))
    listplace(7,7,Rook("b","R",7,7))
    listplace(0,1,Knight("w","N",0,1))
    listplace(0,6,Knight("w","N",0,6))
    listplace(7,6,Knight("b","N",7,6))
    listplace(7,1,Knight("b","N",7,1))
    listplace(0,2,Bishop("w","B",0,2))
    listplace(0,5,Bishop("w","B",0,5))
    listplace(7,2,Bishop("b","B",7,2))
    listplace(7,5,Bishop("b","B",7,5))
    listplace(0,4,Queen("w","Q",0,4))
    listplace(7,4,Queen("b","Q",7,4))
    listplace(7,3,King("b","K",7,3))
    listplace(0,3,King("w","K",0,3))
    show(board)
setuppieces()
#-----------------------------------------------------------------
turn = 0
def play(newmove):#jouer un coup
    global turn#on vérifie le tour, pas de doubles coups !
    if turn % 2 == 0:
        colorturn = "w"
    else:
        colorturn = "b"
    x = newmove
    indexofthing = (length.index(x[0]),height.index(x[1]))
    indexofmove = (length.index(x[2]),height.index(x[3]))
    if internalboard[indexofthing[1]][indexofthing[0]] != "__" and internalboard[indexofthing[1]][indexofthing[0]].showcolor()  == colorturn:#si la pièce existe
        mover = internalboard[indexofthing[1]][indexofthing[0]]
        mover.move(indexofmove[0],indexofmove[1],mover.getmoverange())
        show(board)
        turn += 1
    else:
        None

#combinaison mat rapide: c2c3 d7d6 b2b4 e8a4 h2h3 a4d1