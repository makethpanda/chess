import tkinter as tk
import os 
import chessmod
dir_path = os.path.dirname(os.path.realpath(__file__))
class GameBoard(tk.Frame):
    def __init__(self, parent, rows=8, columns=8, size=64, color1="white", color2="blue"):
        #on initialise un échequier fille de tk.frame"
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}
    
        canvas_width = columns * size
        canvas_height = rows * size + 100

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # ici on regle le raffraichissement de la fenetre a chaque fois qu'on la change de taille
        self.canvas.bind("<Configure>", self.refresh)

    def addpiece(self, name, image, row=0, column=0):
        #on ajoute une pièce dans la mémoire, on essaye de la placer
        self.canvas.create_image(0,0, image=image, tags=(name, "piece"), anchor="c")
        self.placepiece(name, row, column)

    def placepiece(self, name, row, column):
        #on place la pièce sur l'échequier
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)

    def refresh(self, event):
        #on redessine le board, fonction aussi appelé lors de la première création
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")
        

if __name__ == "__main__":#notre boucle principale, dans un "if __name__ == "__main__":" pour éviter des erreurs avec les classes 
    root = tk.Tk()
    board=GameBoard(root)
    def boardplace():#on place toutes les pièces sur l'échequier 
        x = 1 # je ne sait pas pourquoi mais si je commence sur x = 0 tout plante
        for i in range(8):
            for j in range(8):
                if chessmod.getboard()[i][j] == "Bb":
                    board.addpiece(str(x), bb, i,j)
                    x+=1# meme chose pour tout les x+=1
                elif chessmod.getboard()[i][j] == "Nb":
                    board.addpiece(str(x), bh, i,j)
                    x+=1
                elif chessmod.getboard()[i][j] == "Kb":
                    board.addpiece(str(x), bk, i,j)
                    x+=1
                elif chessmod.getboard()[i][j] == "pb":
                    board.addpiece(str(x), bp, i,j)
                    x+=1
                elif chessmod.getboard()[i][j] == "Qb":
                    board.addpiece(str(x), bq, i,j)
                    x+=1
                elif chessmod.getboard()[i][j] == "Rb":
                    board.addpiece(str(x), br, i,j)
                    x+=1
                elif chessmod.getboard()[i][j] == "Bw":
                    board.addpiece(str(x), wb, i,j)
                    x+=1
                elif chessmod.getboard()[i][j] == "Nw":
                    board.addpiece(str(x), wh, i,j)
                    x+=1
                elif chessmod.getboard()[i][j] == "Kw":
                    board.addpiece(str(x), wk, i,j)
                    x+=1
                elif chessmod.getboard()[i][j] == "pw":
                    board.addpiece(str(x), wp, i,j)
                    x+=1
                elif chessmod.getboard()[i][j] == "Qw":
                    board.addpiece(str(x), wq, i,j)
                    x+=1
                elif chessmod.getboard()[i][j] == "Rw":
                    board.addpiece(str(x), wr, i,j)
                    x+=1
    def get(event):# sur chaque nouvelle instruction, on refresh le board en le détruisant puis reconstruisant 
        global board
        board.destroy()
        board = GameBoard(root)
        board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
        chessmod.play(event.widget.get())
        boardplace()
        if chessmod.kingisdead() == True:
            a.config(text="GAME OVER")
    def restart():# on remet le board en position initialle 
        global board
        board.destroy()
        board = GameBoard(root)
        chessmod.setuppieces()# on reset notre script d'échecs aussi
        board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
        boardplace()
        

    e = tk.Entry(root, width=25)
    e.bind('<Return>', get)
    e.pack()
    
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    bb = tk.PhotoImage(file='assets\Bb.png')#toutes les images utilisées
    bh = tk.PhotoImage(file='assets\Bh.png')
    bk = tk.PhotoImage(file='assets\Bk.png')
    bp = tk.PhotoImage(file='assets\Bp.png')
    bq = tk.PhotoImage(file='assets\Bq.png')
    br = tk.PhotoImage(file='assets\Br.png')
    wb = tk.PhotoImage(file='assets\Wb.png')
    wh = tk.PhotoImage(file='assets\Wh.png')
    wk = tk.PhotoImage(file='assets\Wk.png')
    wp = tk.PhotoImage(file='assets\Wp.png')
    wq = tk.PhotoImage(file='assets\Wq.png')
    wr = tk.PhotoImage(file='assets\Wr.png')
    boardplace()
    root.title("chess")
    a = tk.Label(root, text="game in progress")
    tk.Button(root, text="restart game", command=restart).pack()
    a.pack()
    root.mainloop()