from tkinter import *
import math,random



def racket():#Dessine la raquette             
    global xd,yd,cote,racket,rack
    racket=can.create_rectangle(xd,yd,xd+9*cote,yd+cote,fill='red',tag='rack')

def balle():#Dessine la balle
    global balle,x,y,rayon,coul1,coul2,balle,ball
    balle=can.create_oval(x-rayon,y-rayon,x+rayon,y+rayon,fill=coul1,outline=coul2,tag='ball')

def mouv(event):#Gère les mouvements horizontaux de la raquette
    global racket,largeur
    touche=event.keysym
    x=0
    L=can.coords(racket)
    if touche=='Left' and 0<L[0]:
        x=-20
    elif touche=='Right'and L[2]<largeur:
        x=+20
    can.move(racket,x,0)

def mouvball():
    """ Déplacement de la balle """
    global x,y,dx,dy,rayon,largeur,hauteur,imp,L,B,choc1,choc2

    
    L=can.coords(racket)
    B=can.coords(brique)


    # rebond à droite
        if x+rayon+dx>largeur:
        x=largeur-rayon
        dx=-dx
    # rebond à gauche
    if x-rayon+dx<0:
        x=rayon
        dx=-dx
    # rebond en bas
    if y+rayon+dy>hauteur:
        y=hauteur-rayon
        dy=-dy
    # rebond en haut
    if y-rayon+dy < 0:
        y=rayon
        dy=-dy
    # rebond sur la raquette
    if L[0] - 4 <= x <= L[2] + 4 and 570 <= y <= 576:
        can.bell()
        dy = -dy  
    if imp != 3:
        if B[0] - 4 <= x <= B[2] + 4 and B[1] <= y <= B[3]:
            dy = -dy
            imp += 1
            if imp == 1:
                can.itemconfig(brique,fill=choc1)
            if imp == 2:
                can.itemconfig(brique,fill=choc2)
            if imp == 3:
                can.delete(brique)
    
    x = x+dx
    y = y+dy
    
    # affichage
    can.move(balle,dx,dy)

    # mise à jour toutes les 50 ms
    can.after(10,mouvball)

def brique():
    global brique,imp
    brique = can.create_rectangle(350,350,450,380,fill='green',tag='brique')
    imp = 0

def mobric():
    global dpb
    if B[0] < 0:
        dpb=-dpb
    if B[2] > largeur:
        dpb=-dpb
    can.move(brique,dpb,0)
    can.after(25, mobric)

def surprise():
    global pal,choc1,choc2,brique,brick,rack,racket
    can.itemconfig(balle,fill=pal[random.randrange(len(pal))])
    can.itemconfig(racket,fill=pal[random.randrange(len(pal))])
    can.itemconfig(brique,fill=pal[random.randrange(len(pal))])
    choc1 = pal[random.randrange(len(pal))]
    choc2 = pal[random.randrange(len(pal))]
    fen.itemconfig(can,bg=pal[random.randrange(len(pal))])

#Initialisation des variables   
cote,xd,yd=10,360,580
largeur,hauteur,rayon=630,630,8
x,y=380,540
pal=["yellow","blue","red","green","pink","purple","brown","cyan","white","black"]
# direction initiale
dx = 2
dy = -2
dpb = 5
coul1='red'
coul2='black'
choc1='yellow'
choc2='black'

#Mise en place de la fenêtre
fen=Tk()
fen.title('Racket')
can=Canvas(fen,bg='blue',width=largeur,height=hauteur)
can.pack()
fen.bind("<Key>",mouv)
bou1 = Button(fen,text='Quitter',command=fen.destroy)
bou1.pack(side=RIGHT)
bou2=Button(fen,text='Raquette',command=racket)
bou2.pack(side=LEFT)
bou3=Button(fen,text='Balle',command=balle)
bou3.pack(side=LEFT)
bou3=Button(fen,text='Go',command=mouvball)
bou4=Button(fen,text='Brique',command=brique)
bou5=Button(fen,text='Obstacle mouvant',command=mobric)
bounus=Button(fen,text='Surprise!',command=surprise)
bou4.pack(side=LEFT)
bou3.pack(side=LEFT)
bounus.pack(side=LEFT)
bou5.pack(side=LEFT)


fen.mainloop()
