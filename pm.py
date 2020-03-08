from random import *

nb = randint(0,1000)
c=0
dev=(-1)
while dev != nb:
    dev=int(input("Entrer un nombre entre 0 et 1000:  "))
    if dev<0 or dev>1000:
        print("On veut un nombre entre 0 et 1000")
    if dev>0 or dev<1000:
        if dev<nb:
            if nb-dev>=100:
                print("C'est beaucoup plus")
            if nb-dev>=10 and nb-dev<100:
                print("C'est plus")
            if nb-dev<10:
                print("C'est un tout petit peu plus")
        if dev>nb:
            if dev-nb>=100:
                print("C'est beaucoup moins")
            if dev-nb>=10 and dev-nb<100:
                print("C'est moins")
            if dev-nb<10:
                print("C'est un tout petit peu moins")
    c+=1
    if dev==nb:
        print("Bravo! La reponse etait",nb)
        print("Trouve en",c,"essais.")
        break

