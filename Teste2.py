#Teste 2
#Importando Biblioteca Math
import math
#Definindo lista de Vetores
vetor = []
for e in range(0,10):
    # Condicional 1 -> Defini se é Par
    if e % 2 ==0:
        #Formula1
        x = (3**e) + (7*math.factorial(e))
        vetor.append(x)
    # Condicional 2 -> Afirma que é impar
    else: 
        #Formula2
        x = (2**e) + (4*math.log(e))
        vetor.append(x)
#Ponto Máximo
max_vetor = max(vetor)
#Ponto Médio
med_vetor = sum(vetor)/len(vetor)
print(f"A posição do maior elemento é {max_vetor} e a média dos elementos contidos nesse vetor é de {med_vetor:.2f}")
