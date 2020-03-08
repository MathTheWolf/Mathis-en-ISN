from tkinter import*
from tkinter import messagebox
from random import*
import math


def racket():
    global xd,yd,cote,racket
    racket = can1.create_rectangle(xd,yd,xd+2*cote,yd+0.5*cote,fill='green',tag='rack')

def move(event):
    global racket,largeur
    touche=event.keysym
    x=0
    L=can1.coords(racket)
    if touche=='Left' and 0<L[0]:
        x=-20
    elif touche=='Right'and L[2]<largeur:
        x=+20
    can1.move(racket,x,0)
    


def bouge():
    global dy,y,dx,x,bcx,bcy
    bcx=['','']
    bcy=['','']
    owo = can1.coords(oval1)
    bcx = [owo[0],owo[2]]
    bcy = [owo[1],owo[3]]
    
    if bcy[0]<0 or bcy[1]>500:
        dy=-dy
    if bcx[0]<0 or bcx[1]>500:
        dx=-dx
    for i in range(0,len(coord)):
        if dy>0:
            if coord[i][1]<=bcy[1]<=coord[i][3] and ((bcx[0]+bcx[1])//2) in range(int(coord[i][0]),int(coord[i][2])):
                dy=-dy
                can1.delete(obs[i])
                coord.pop(i)
                obs.pop(i)
                break
        if dy<0:
            if coord[i][1]<=bcy[0]<=coord[i][3] and ((bcx[0]+bcx[1])//2) in range(int(coord[i][0]),int(coord[i][2])):
                dy=-dy
                can1.delete(obs[i])
                coord.pop(i)
                obs.pop(i)
                break
        if dx>0:
            if ((bcy[0]+bcy[1])//2) in range(int(coord[i][1]),int(coord[i][3])) and bcx[1]==coord[i][0]:
                dx=-dx
                can1.delete(obs[i])
                coord.pop(i)
                obs.pop(i)
                break
        if dx<0:
            if ((bcy[0]+bcy[1])//2) in range(int(coord[i][1]),int(coord[i][3])) and bcx[0]==coord[i][2]:
                dx=-dx
                can1.delete(obs[i])
                coord.pop(i)
                obs.pop(i)
                break
    


        
        


    y=y+dy
    x=x+dx
    can1.move(oval1,dx,dy)
    can1.after(10,bouge)

##########################################
x1,y1=250,400
rayon=10
cote,xd,yd=40,230,450
vitesse=uniform(1.8,2)*5
angle=uniform(0,2*math.pi)
dy=-abs(0.75 * vitesse * math.sin(angle))
y=400
dx=abs(0.75 * vitesse * math.cos(angle))
x=250
largeur=500
hauteur=500

fen1=Tk()
fen1.title("Exercice d'animation avec Tkinter")

can1=Canvas(fen1,bg='dark grey',height=hauteur,width=largeur)
can1.pack(side=LEFT)
oval1=can1.create_oval(x1-rayon,y1-rayon,x1+rayon,y1+rayon,width=2,fill='red')
obs=[' ' for o in range(40)]
coord=[a for a in obs]
for i in range(0,10):
    obs[i] = can1.create_rectangle(0+i*50,0,50+i*50,50,fill='blue',tag='brick'+str(i))
    obs[i+10] = can1.create_rectangle(0+i*50,50,50+i*50,100,fill='purple',tag='brick'+str(i+10))
    obs[i+20] = can1.create_rectangle(0+i*50,100,50+i*50,150,fill='pink',tag='brick'+str(i+20))
    obs[i+30] = can1.create_rectangle(0+i*50,150,50+i*50,200,fill='yellow',tag='brick'+str(i+30))
    coord[i] = can1.coords(obs[i])
    coord[i+10] = can1.coords(obs[i+10])
    coord[i+20] = can1.coords(obs[i+20])
    coord[i+30] = can1.coords(obs[i+30])
racket()
fen1.bind("<Key>",move)
#move()
Button(fen1,text='Quitter',command=fen1.quit).pack(side=BOTTOM)
Button(fen1,text='Bouge',command=bouge).pack()


fen1.mainloop()
#messagebox.showinfo('Message',"A bientôt")
fen1.destroy()
