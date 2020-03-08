from turtle import*
from random import*

while True:
    dico=["informatique"]

    while True:
        choix=input("Chosir le mot? (Oui/Non)")
        if choix == "Oui":
            mot=input("Mot ? : ")
            break
        elif choix == "Non":
            mot=dico[randint(0,0)]
            break

    clear()
    word=' '
    motl=[a for a in mot]
    pendu=[" _ " for a in mot]
    alpha='abcdefghijklmnopqrstuvwxyz'
    alpha=[a for a in alpha]
    #interdit=[' ','_','é','è',]
    victoire = 0
    tries = 0
    fails = 0

    def dessin(fails):
        if fails == 1:
            goto(-50,0)
            fd(100)
            up()
        if fails == 2:
            goto(0,0)
            lt(90)
            down()
            fd(230)
            up()
        if fails == 3:
            rt(90)
            down()
            fd(70)
            up()
        if fails == 4:
            rt(90)
            down()
            fd(50)
            up()
        if fails == 5:
            rt(90)
            down()
            circle(20)
            up()
        if fails == 6:
            lt(90)
            fd(40)
            down()
            fd(70)
            up()
        if fails == 7:
            lt(45)
            down()
            fd(70)
            up()
            fd(-70)
            rt(45)
        if fails == 8:
            rt(45)
            down()
            fd(70)
            up()
            fd(-70)
            lt(45)
        if fails == 9:
            fd(-30)
            lt(90)
            fd(-30)
            down()
            fd(60)
            up()
        
    while pendu != motl:
        letter = input("Lettre ? : ")
        i = 0
        tries +=1
        print("On en est a l'essai",tries)
        if len(letter) <= 1:
            if letter not in alpha:
                print("Ce caractère est deja propose ou interdit")
                continue
            for i in range(len(motl)):
                    if letter == motl[i]:
                        pendu[i] = motl[i] 
                        word=''
                        for i in range(len(motl)):
                            word+=pendu[i]+' '
                    for a in range(len(alpha)):
                            if letter == alpha[a-1]:
                                del alpha[a-1]
            if letter not in motl:
                print("Non!")
                fails+=1
                dessin(fails)
        else:
            print('Une lettre a la fois')
            continue
        if pendu != motl and fails == 10: 
                print("Pendu! Le mot etait", mot,".")
                break
        
        print(word)
        print("Lettres non utilisees:", alpha)
        print("Le nombre de fautes est de", fails)

        

    print("Victoire! Le mot etait",mot,", trouve en",tries,"essai(s)")
        
    rp = input("Rejouer? (Oui/Non)")
    if rp == "Oui":
        continue
    if rp == "Non":
        break
    

