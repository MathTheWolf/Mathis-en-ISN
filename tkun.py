  # Petit exercice utilisant la bibliothèque graphique Tkinter
from tkinter import *
from random import randrange
# --- définition des fonctions gestionnaires d'événements : ---

def ligne():
    #Tracé d'une ligne dans le canevas can1
    global x1,y1,x2,y2, coul
    can.create_line(x1,y1,x2,y2,width=2,fill=coul)
    # modification des coordonnées pour la ligne suivante :
    y1, y2 = y1+10, y2-10
    
def croix():
    #Tracé d'une croix dans le canevas
    global x3,y3,x4,y4,x5,y5,x6,y6
    can.create_line(x3,y3,x4,y4,width=3,fill='red')
    can.create_line(x5,y5,x6,y6,width=3,fill='red')


def couleur():
    #"Changement aléatoire de la couleur du tracé"
    global coul
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c = randrange(8) # => génère un nombre aléatoire de 0 à 7
    coul= pal[c]

def carre():
    global coul
    can.create_rectangle(50,50,100,70,width=6,fill=coul)

#------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
x1, y1, x2, y2 = 10, 490, 490, 10# coordonnées de la ligne
x3,y3,x4,y4=10,250,490,250
x5,y5,x6,y6=250,10,250,490
coul = 'dark green' # couleur de la ligne
# Création du widget principal ("maître") :
fen = Tk()
# création des widgets "esclaves" :
can = Canvas(fen,height=500,width=500,bg='dark grey')
can.pack(side=RIGHT)
bou1 = Button(fen,text='Quitter',command=fen.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen,text='Tracer une ligne',command=ligne)
bou2.pack()
bou3 = Button(fen,text='Autre couleur',command=couleur)
bou3.pack()
bou4 = Button(fen,text='cible',command=croix)
bou4.pack()
bou5 = Button(fen,text='Rectangle',command=carre)
bou5.pack()
fen.mainloop() # démarrage du réceptionnaire d'événements
fen.destroy() # destruction (fermeture) de la fenêtre
