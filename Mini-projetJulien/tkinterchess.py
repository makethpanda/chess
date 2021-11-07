import tkinter as tk
import os 
import chessmod
dir_path = os.path.dirname(os.path.realpath(__file__))
class GameBoard(tk.Frame):
    def __init__(self, parent, rows=8, columns=8, size=64, color1="white", color2="blue"):
        '''size is the size of a square, in pixels'''
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

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    def addpiece(self, name, image, row=0, column=0):
        '''Add a piece to the playing board'''
        self.canvas.create_image(0,0, image=image, tags=(name, "piece"), anchor="c")
        self.placepiece(name, row, column)

    def placepiece(self, name, row, column):
        '''Place a piece at the given row/column'''
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)

    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''
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
        

if __name__ == "__main__":
    x = 0
    root = tk.Tk()
    board = []
    board.append(GameBoard(root))
    board[x].pack(side="top", fill="both", expand="true", padx=4, pady=4)
    bb = tk.PhotoImage(file='assets\Bb.png')
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
    def boardplace():
        for i in reversed(range(8)):
            for j in reversed(range(8)):
                if chessmod.getboard()[i][j] == "Bb":
                    board[x].addpiece("bbishop"+str(i+j), bb, i,j)
                elif chessmod.getboard()[i][j] == "Nb":
                    board[x].addpiece("bnight"+str(i+j), bh, i,j)
                elif chessmod.getboard()[i][j] == "Kb":
                    board[x].addpiece("bking"+str(i+j), bk, i,j)
                elif chessmod.getboard()[i][j] == "pb":
                    board[x].addpiece("bpawn"+str(i+j), bp, i,j)
                elif chessmod.getboard()[i][j] == "Qb":
                    board[x].addpiece("bqueen"+str(i+j), bq, i,j)
                elif chessmod.getboard()[i][j] == "Rb":
                    board[x].addpiece("brook"+str(i+j), br, i,j)
                elif chessmod.getboard()[i][j] == "Bw":
                    board[x].addpiece("wbishop"+str(i+j), wb, i,j)
                elif chessmod.getboard()[i][j] == "Nw":
                    board[x].addpiece("wnight"+str(i+j), wh, i,j)
                elif chessmod.getboard()[i][j] == "Kw":
                    board[x].addpiece("wking"+str(i+j), wk, i,j)
                elif chessmod.getboard()[i][j] == "pw":
                    board[x].addpiece("wpawn"+str(i+j), wp, i,j)
                elif chessmod.getboard()[i][j] == "Qw":
                    board[x].addpiece("wqueen"+str(i+j), wq, i,j)
                elif chessmod.getboard()[i][j] == "Rw":
                    board[x].addpiece("wrook"+str(i+j), wr, i,j)
    boardplace()
    def get(event):
        global board
        global x
        x+= 1
        chessmod.play(event.widget.get())
        for widgets in board[x-1].winfo_children():
            widgets.destroy()
        board[x-1].destroy()
        board.append(GameBoard(root))
        board[x].pack(side="top", fill="both", expand="true", padx=4, pady=4)
        boardplace()
    root.title("chess")
    e = tk.Entry(root, width=25)
    e.bind('<Return>', get)
    e.pack()

    root.mainloop()