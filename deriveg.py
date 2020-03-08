from random import*

alleles=['J','R','B','V','M','N']
generations=0

while True:
    tirage=[]
    generations+=1
    gen=[' ',' ',' ',' ',' ',' ']
    for i in range(len(alleles)):
        for j in range(randint(0,6)):
            tirage.append(alleles[i])
    for i in range(6):
        gen[i] = tirage[randint(0,len(tirage)-1)]
    if all(a == gen[0] for a in gen):
        break
             
print(generations)
print(gen)

