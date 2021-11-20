# Teste 3
#Definindo Dicionario de Notas
notas = {}
for e in range(0,5):
    nota = input("Adicione a Nota: ")
    nome = input("Nome do Aluno: ")
    notas[nome] = nota
#Adquire Valores do Dicionario
values = notas.values()
#Adquire Valor máximo
max_value = max(values)
for indice in notas:
    #Se a Nota máxima de certo indice == Máxima Geral
    if notas[indice] == max_value:
        #Grave esse indice
        index = indice
        break
print(f"O aluno com maior nota é {index} e sua respectiva nota: {max_value}")