def clettre(lettre):
    lc=""
    if lettre == ' ':
        code+=' '
    if lettre == '':
        code+='A'
    elif mot[i] != ' ':    
        code+=chr(ord(mot[i])+1)
    return code

def unshift(code):
    mot=code
    code=""s
    for i in range(len(mot)):
        if mot[i] == ' ':
            code+=' '
        if mot[i] == 'A':
            code+='Z'
        elif mot[i] != ' ':   
            code+=chr(ord(mot[i])-1)
    return code

print(shift('LES CARROTTES SONT CUITES'))
print(unshift('MFT DBSSPUUFT TPOU DVJUFT'))
