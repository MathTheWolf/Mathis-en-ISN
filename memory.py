from tkinter import *
from random import *
import time


global deck,rect,comp,valid,colors,back
deck=[]
rect=[[],[]]
comp=['','']
valid=[]
colors=["yellow","blue","red","green","pink","purple","brown","cyan"]
pal=[]
choice = 1
back=[[50,50,200,250],[300,50,450,250],[550,50,700,250],[800,50,950,250],[50,450,200,650],[300,450,450,650],[550,450,700,650],[800,450,950,650]]

global m



m = 0

def shuf():
    global pal,deck
    deck=[]
    if choice == 1:
        pal=["yellow","blue","red","green"]
    if choice == 2:
        pal=["pink","purple","brown","cyan"] 
    for i in range(len(pal)):
        for j in range(2):
            deck.append(pal[i])
    shuffle(deck)

def start():
    global rect,comp,valid
    shuf()
    rect=[[],[]]
    comp=['','']
    valid=[]
    Prompt.pack_forget()
    Oui.pack_forget()
    Non.pack_forget()
    Start.pack_forget()
    Quit.pack_forget()
    Opt.pack_forget()
    Main.pack(side=TOP,fill=X)
    Quit.pack(side=TOP,fill=X)
    Canevas.pack()
    Canevas.bind('<Button-1>', processus)
    for i in range(0,4):
        Canevas.create_rectangle(50+i*250,50,200+i*250,250,fill='black')
        Canevas.create_rectangle(50+i*250,450,200+i*250,650,fill='black')


    

    

    
def processus(event):
    global m,comp,rect,valid,deck,Prompt,Oui,Non
    Prompt = Label(fen,text="Bravo! Rejouer?")
    Oui = Button(fen,text="Oui",command=start)
    Non = Button(fen,text="Non",command=retour)
    if m < 2:
        if event.x in range(50,200) and event.y in range(50,250) and [50,50,200,250] not in valid:
            Canevas.create_rectangle(50,50,200,250,fill=deck[0])
            comp[m]=deck[0]
            rect[m]=[50,50,200,250]
        
        if event.x in range(300,450) and event.y in range(50,250) and [300,50,450,250] not in valid:
            Canevas.create_rectangle(300,50,450,250,fill=deck[1])
            comp[m]=deck[1]
            rect[m]=[300,50,450,250]
            
        if event.x in range(550,700) and event.y in range(50,250) and [550,50,700,250] not in valid:
            Canevas.create_rectangle(550,50,700,250,fill=deck[2])
            comp[m]=deck[2]
            rect[m]=[550,50,700,250]
            
        if event.x in range(800,950) and event.y in range(50,250) and [800,50,950,250] not in valid:
            Canevas.create_rectangle(800,50,950,250,fill=deck[3])
            comp[m]=deck[3]
            rect[m]=[800,50,950,250]
            
        if event.x in range(50,200) and event.y in range(450,650) and [50,450,200,650] not in valid:
            Canevas.create_rectangle(50,450,200,650,fill=deck[4])
            comp[m]=deck[4]
            rect[m]=[50,450,200,650]
            
        if event.x in range(300,450) and event.y in range(450,650) and [300,450,450,650] not in valid:
            Canevas.create_rectangle(300,450,450,650,fill=deck[5])
            comp[m]=deck[5]
            rect[m]=[300,450,450,650]
            
        if event.x in range(550,700) and event.y in range(450,650) and [550,450,700,650] not in valid:
            Canevas.create_rectangle(550,450,700,650,fill=deck[6])
            comp[m]=deck[6]
            rect[m]=[550,450,700,650]
            
        if event.x in range(800,950) and event.y in range(450,650) and [800,450,950,650] not in valid:
            Canevas.create_rectangle(800,450,950,650,fill=deck[7])
            comp[m]=deck[7]
            rect[m]=[800,450,950,650]
        
        if event.x and event.y not in back:
            pass
        if m != 2:
            m+=1
    if m == 2:
        fen.after(500,test)
    

def test():
    global comp,rect,m,valid
    if comp[0]==comp[1] and rect[0]!=rect[1]:
        for i in range(2):
            valid.append(rect[i])
            Canevas.create_rectangle(rect[i][0],rect[i][1],rect[i][2],rect[i][3],fill="white")
        m = 0
        comp=['','']
        rect=[[],[]]
    elif rect[0]!=rect[1]:
        m = 0
        Canevas.create_rectangle(rect[0][0],rect[0][1],rect[0][2],rect[0][3],fill="black")
        Canevas.create_rectangle(rect[1][0],rect[1][1],rect[1][2],rect[1][3],fill="black")
        comp=['','']
        rect=[[],[]]
    else:
        print("Pas deux fois la même carte d'affilee!")
        m = 1
        comp=[comp[0],'']
        rect=[rect[0],[]]
    if len(valid) == 8:
        m=0
        comp=['','']
        rect=[[],[]]
        valid=[]
        deck=[]
        Canevas.pack_forget()
        Quit.pack_forget()
        Main.pack_forget()
        Prompt.pack(side=TOP)
        Oui.pack(side=LEFT)
        Non.pack(side=RIGHT)


    







def init():
    global Start,Opt,Quit,Pal1,Pal2,Ret,Main,Prompt,Oui,Non,Canevas
    Ret = Button(fen,text="Retour au menu principal",command=retour)
    Pal1 = Button(fen, text="Palette de couleurs 1 (Jaune, Rouge, Bleu, Vert)",command=pal1)
    Pal2 = Button(fen, text="Palette de couleurs 2 (Violet, Rose, Marron, Cyan)",command=pal2)
    Start = Button(fen, text="Commencer", command=start)
    Start.pack(side=TOP,fill=X)
    Opt = Button(fen, text="Options", command=options)
    Opt.pack(side=TOP,fill=X)
    Quit = Button(fen, text="Quitter", command=fen.destroy)
    Quit.pack(side=TOP,fill=X)
    Main = Button(fen, text="Menu Principal", command=retour)
    Pal1.pack_forget()
    Pal2.pack_forget()
    Ret.pack_forget()
    Prompt = Label(fen,text="Bravo! Rejouer?")
    Oui = Button(fen,text="Oui",command=start)
    Non = Button(fen,text="Non",command=retour)
    Canevas = Canvas(fen,height=1000,width=1000,bg="gray")
     

def options():
    Start.pack_forget()
    Opt.pack_forget()
    Quit.pack_forget()
    Ret.pack(fill=X)
    Pal1.pack(fill=X)
    Pal2.pack(fill=X)
    
def retour():
    global deck,rect,comp,valid
    deck=[]
    rect=[[],[]]
    comp=['','']
    valid=[]
    Start.pack(side=TOP,fill=X)
    Opt.pack(side=TOP,fill=X)
    Quit.pack_forget()
    Quit.pack(side=TOP,fill=X)
    Canevas.pack_forget()
    Main.pack_forget()
    Pal1.pack_forget()
    Pal2.pack_forget()
    Ret.pack_forget()
    Prompt.pack_forget()
    Oui.pack_forget()
    Non.pack_forget()



def pal1():
    global choice,deck
    choice = 1
    deck=[]

def pal2():
    global choice,deck
    choice = 2
    deck=[]


fen=Tk()
fen.title("Memory")
init()


fen.mainloop()
