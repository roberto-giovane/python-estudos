# While
# Enquanto for verdadeiro, vai ficar em loop infinito !!!

#numeroSecreto = 8
#palpite = int(input('Escolha um numero: '))

#while palpite != numeroSecreto:
   # print('Hahahaha errou !!!')
   # palpite = int(input('Escolha um numero: '))

#print('\nUfa.... até que enfim..')

#########################################################

# jogo de um ponto para cada numero par digitado
# um ponto negativo para cada numero impar

# Placar

certo = 0
errado = 0
print('''
      jogo de numero par...o
      digite varios valores e
        .-=-.   .-=-.   .-=-.  
      /     \ /     \ /     \ 
     |       |       |       |
      \    ./=\.   ./=\.    / 
       '-=/'   '\-/'   '\=-'  
         |       |       |    
          \     / \     /     
   jgs     '-=-'   '-=-'      6        

'''
)
palpite = int(input('Digite seu numero par: '))

while True:
    if palpite == 0:
        print ('certo numero par')
        break
    elif palpite % 2 ==0:
        print('certo numero par !')
        # certo = certo + 1
        certo += 1
        palpite = int(input('Digite outro numero par: '))
    elif palpite % 2 == 1:
        print('errou meu, digite um numero par....')
        print('aff.. ganhou um ponto negativo')
        errado +=1
        palpite = int(input('Digite seu numero par: '))

total = certo + errado
conta = certo / total
print('\nresultado do jogo: ')
print(f'total de palpites: ')
print(f'        acertos: {certo}')
print(f'        erros: {certo}')


print(f'\nporcentagem de acertos: {conta: 2%}\n')