<div id="top"></div>


[![Issues][issues-shield]][issues-url]



<br />
<div align="center">
  <a href="https://github.com/makethpanda/chess">
    
  </a>

  <h3 align="center">Chess</h3>

  <p align="center">
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">Explication du projet</a>
      <ul>
        <li><a href="#Exemples-de-code">explications de code</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Comment jouer</a>
      <ul>
        <li><a href="#prerequisites">Prerequis</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Le theme de ce mini projet est un jeu d'échecs fonctionnel en python avec une interface graphique. 
Il faut coder:
toutes les pièces, 
les conditions de victoires, 
la GUI 
ainsi qu'une façon de recommencer le jeu

<p align="right">(<a href="#top">back to top</a>)</p>





<!-- GETTING STARTED -->
## Getting Started

Voici comment télécharger
### Prerequisites

python, tkinter

### Installation

_Voici comment faire fonctionner le jeu._

allez sur la page https://github.com/makethpanda/chess/releases et téléchargez la plus récente.

dézippez et ouvrez "tkinterchess.py" dans votre éditeur de code préféré et exécutez le code.

entrez des commandes de mouvement, tel que a2a3 ert appuyez sur Enter pour les exécuter

l'échequier est formé de cette façon:

 1    a     b     c     d     e     f     g     h
 
 2
 
 3
 
 4
 
 5
 
 6
 
 7
 
 8
 
 
 
 voici une combinaison de mat rapide: 
 
 c2c3 d7d6 b2b4 e8a4 h2h3 a4d1
 
 toutes les pièces ont été testées et fonctionnent parfaitement.
 
 notons que pour effectuer un mat il faut manger le roi adverse.
 
<p align="right">(<a href="#top">back to top</a>)</p>

### Exemples de code

Ce mini projet à été construit avec python, ainsi que l'extension tkinter< nousd allons ici analyser en plus de détails certaines parties du code 

<p align="right">(<a href="#top">back to top</a>)</p>


```python
internalboard =  [ ["__" for i in range(8)] for _ in range(8) ]
board = [ ["__" for i in range(8)] for _ in range(8) ]
```
voici le setup de notre échequier, nous utilisons un échequier dit "externe" (board) pour représenter ce que l'utilisateur voit, et un echequier 

dit "interne" pour stocker chaque objet a sa bonne place et pouvoir l'appeler depuis sa place

```python
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
        return 
    def showcolor(self):
        return self.color
```

voici notre classe mère, pièce, chaque pièce du jeu à beaucoup de comportements en communs, tel que leurs mouvmenets et leur init, ainsi qu'une fonction show pour 
l'échequier externe 
