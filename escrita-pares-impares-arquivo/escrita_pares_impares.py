# TODO: Crie um método que irá gravar os números de 0 a 100 em dois arquivos, no arquivo "impares.txt" grave os números ímpares e
# no arquivo "pares.txt" grave os números pares.
# IMPORTANTE: Este exercício não tem teste (pytest) por isso use sua criatividade para criar a sua agenda.

#def escrever_pares_impares():
    #pares = open ('pares.txt', 'w')
    #impares =open ('impares.txt', 'w')

    #for numeros in range (101):
        #if numeros % 2 == 0:
         #pares.write('{}'.format(numeros) + ',')
    #else:
        #impares.write ('{}', format(numero) + ',')

        #pares.close
        #impares.close

def escrever_pares_impares():
    impares = open ('impares.txt', 'a')
    with open ('pares.txt', 'a') as pares:
        for numero in range (0, 101):
            if numero % 2 == 0:
                pares.write (str(numero))
                pares.write ('/n')
            else:
                impares.write(str(numero))
                impares.write('/n')
    impares.close()

    print (impares)



   