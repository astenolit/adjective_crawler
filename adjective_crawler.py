## The Adjective Crawler for Books
######################################################
##
## Enrique Contreras (enconva@gmail.com)
##
## This code is under the Creative Commons CC BY-NC-SA license
##
######################################################

## First, procedures for opening files.
## Note that I've defined two different procedures for each file
## as each file needs a different splitting mode.

def abrir_libro (archivo):
    with open(archivo, 'r') as f:
         libro = f.read ().lower ()
         libro_splitted = split_string (libro,' ,.;:-\'\"?!_\n\t')
         
    return libro_splitted

def abrir_adjetivos (archivo):
    with open(archivo, 'r') as f:
         adjectives = f.read ()
         adjectives = adjectives.split ()     
    return adjectives

## Splitting the book. From Udacity cs101.
def split_string (source,splitlist):
    output = []
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                output [-1] = output [-1] + char
    return output

## This is the main procedure.
## Its inputs are:
##      archivo -> a book in .txt format.
##      cadena -> a string to find.
##      field -> the range of adjectives before and after the string.
##      letters -> minimum amount of letters for counting it as an adjective.
##
## The ouput is displayed on screen; it's also possible
## to add a return statement for the output data.

def adjective_crawler (archivo, cadena, field, letters):
    ## Opening files and setting variables...
    
    adjectives = abrir_adjetivos ('adjectives.txt')
    libro = abrir_libro (archivo)

    target = cadena
    target = target.lower ()
    target = target.split ()    ## In case of multiple words in the search string
    
    numero_palabras = len (libro)
    contador, contexto, recuerda, posicion = 0, {}, [], [0,0,0]
    
    for i in range (numero_palabras):
        if i + len (target) < len (libro):
            for n in range (len (target)):
                if libro[i+n] == target [n]:
                    contador = contador  + 1
            if contador == len(target):
                contador = 0
                posicion = posicionar (i, numero_palabras, posicion)
                
                if field > i :
                    contexto = agregar (0, i + (len(target)-1) + \
                                        field, libro, adjectives, contexto, letters)                 
                elif i + (len(target)-1) + field > len(libro):
                    contexto = agregar (i - field, len(libro), \
                                        libro, adjectives, contexto, letters)
                else:
                    contexto = agregar (i - field, i + (len(target)) \
                                        + field, libro, adjectives, contexto, letters)  
            else:
                contador = 0

    resultado = sorted(([value,key] for (key,value) in contexto.iteritems()),reverse = True)
    formato (archivo, cadena, field, numero_palabras, posicion, \
             resultado, letters)

## This is a sub-procedure used inside the main adjective_crawler for saving code.
def agregar (a, b, libro, adjectives, contexto, letters):   
    for t in range (a, b):
        if libro[t] in adjectives and len (libro[t]) >= letters:
            if libro[t] not in contexto: 
                contexto[libro[t]] = 1
            else:
                contexto[libro[t]] = contexto[libro[t]] + 1
    return contexto

## Another sub procedure for locating the string in the text.
## It calculates in which third is the string and returns
## a list with the counts.
def posicionar (i, numero_palabras, posicion):
    if i <= numero_palabras / 3 :
        posicion [0] = posicion [0] + 1
        
    if i > numero_palabras / 3 and i < (numero_palabras / 3 ) * 2:
        posicion [1] = posicion [1] + 1

    if i > (numero_palabras / 3) * 2:
        posicion [2] = posicion [2] + 1

    return posicion

## Formatting and displaying data on the screen.
## It can be skipped for having only raw data.
def formato (archivo, cadena, field, numero_palabras, \
             posicion, resultado, letters):

    #Formatting the data for printing on screen:
    porciento, times = porcentaje (posicion)
    linea = '##' + ' '* 12 + ' Adjective Crawler for Books' \
            + ' '* 12 + ' ##'
    print '#' *  len (linea)
    print linea
    print '#' *  len (linea)
    print ''
    print 'STATISTICS'
    print '**********'
    print 'The file: \'' + archivo + '\' is composed of '\
          + str(numero_palabras), 'words'
    print 'The target string: \'' + cadena + '\' appears ' \
          + str (times) + ' times in the text.'
    print '\t', posicion[0], 'times in the first third of the text (' + \
          str (porciento[0])  + '%)' 
    print '\t', posicion[1], 'times in the second third of the text (' + \
          str (porciento[1]) + '%)'
    print '\t', posicion[2], 'times in the third third of the text (' + \
          str (porciento[2]) + '%)'
    print ''
    print '#' *  len (linea)
    print 'In a range of ' + str(field) + ' word(s) before and after the targetted string,'
    print len (resultado), 'adjectives with at least', letters, 'letters have been founded:'
    print ''

    # printing the list in 2 columns
    if len (resultado) == 0:
        print None
    elif len (resultado) == 1:
        print '\a', (resultado[0][0]), 'times:' , resultado[0][1]
    else:
        if len (resultado) % 2 == 0:                # even number of results
            for n in range (0, len (resultado),2):
                print '\a', (resultado[n][0]), 'times:' , resultado[n][1], \
                      '\t\t', (resultado[n+1][0]), 'times:' , resultado[n+1][1]
        else:                                       # odd number of results
            for n in range (0, len (resultado),2):
                if n == (len (resultado))-1:
                    print '\a', (resultado[n][0]), 'times:' , resultado[n][1]
                else:
                        print '\a', (resultado[n][0]), 'times:' , resultado[n][1], \
                              '\t\t', (resultado[n+1][0]), 'times:' , resultado[n+1][1]                     
    print ''
    print '#' *  len (linea)

## Sub procedure for calculating the percentage of the string in every third
def porcentaje (posicion):
    times = posicion [0] + posicion [1] + posicion [2]
    porciento = [0,0,0]
    if posicion[0] != 0:
        porciento[0] = round ((posicion[0] * 100.) / times,2)
    if posicion[1] != 0:
        porciento[1] = round ((posicion[1] * 100.) / times,2)
    if posicion[2] != 0:
        porciento[2] = round ((posicion[2] * 100.) / times,2)
    return porciento, times

    
## End of code ##

adjective_crawler ('don_quixote_part_1.txt','Dulcinea',2,4)


    
