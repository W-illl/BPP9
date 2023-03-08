import pdb
pdb.set_trace()

lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

lista_maximos = [max(val) for val in lista]

print('Números máximos: ',lista_maximos)

lista2 = [3, 4, 8, 5, 5, 22, 13]

def es_primo(numero):
    primo = True
    for i in range(2, numero):
        if(numero%i == 0):
            primo = False
    return primo

numeros_primos = list(filter(es_primo,lista2))

print('Números primos: ',numeros_primos)