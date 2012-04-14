## Extracting all adjectives from a given dictionary
## and saving them in a file .txt.
######################################################
##
## Enrique Contreras (enconva@gmail.com)
##
## This code is under the Creative Commons CC BY-NC-SA license
##
######################################################

def abrir (archivo):
    with open(archivo, 'r') as f:
        return (f.read ()).split ()

def guardar (archivo, content):
    with open(archivo,'w') as f:
        f.write(content)
        
def take_adjectives (archivo1, archivo2):
    adjetivos = []
    diccionario = abrir (archivo1)
    for i in range (0, len(diccionario)):
        if diccionario[i] == 'a.':
            a = i
            while diccionario[a].isupper () == False:
                a = a - 1
            adjetivos.append (diccionario[a])
            if ';' in diccionario[a-1] and \
               diccionario[a-1][:-1].isupper ():
                adjetivos.append (diccionario[a-1][:-1])

    resultado = ''
    for e in adjetivos:
        resultado = resultado + ' ' + e

    resultado = resultado.lower ()
    guardar (archivo2,resultado)

take_adjectives ('dictionary.txt','adjectives.txt')

