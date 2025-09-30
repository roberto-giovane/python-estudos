#Tuplas
#São listas "IMUTADAS" (não pode se alterada)
#()

diasSemana = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado')
'''
print(diasSemana)

#Imprimir uma posição, lembre-se matriz  começa com 0
print(diasSemana[5])
'''
#####################################################
# Lista é um tipo de lista que pode ser manipuladas


motos = ['srad', 'hunter 350', 'twister 250', 'lander 250']

print(motos)
print(motos[2])

#adicionar um item na lista


motos.append('harley davidson iron 883')
print(motos)
motos.remove('srad')
print(motos)
#motos.pop(3)
#print(motos)
 
motos.sort() 
print

###################################################################

#introdução - laços de repetiços

#for
print()

for dias in diasSemana:
    print(f'{dias}-feira')

print()

for i in motos:
    print(i)

####################################################################################

# Dicionario
# Dicionarios são tipos de lista no formato "chave" : "valor"
# Muito importante para quem trabalha com dados e API
# {}

agendaTelefone = {
    'thiago' : '(11) 9 7281-1432',
    'fabio' : '(11) 9 9999-8888',
    'patricia' : '(11) 9 7777-6666',
}

print(agendaTelefone['patricia'])

print('agenda de contatos')
for i in agendaTelefone:
    print(f'contato:{i}, telefone:{agendaTelefone[i]}')