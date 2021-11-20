# Teste 1
#Definindo Intervalo
intervalo = range(1,5000001)
#Index = Números Pares Multiplos
index = 0 
for numero in intervalo:
    # Condicional do Teste
    if numero % 49 == 0 and numero % 37 ==0:
        index +=1
print(f"A Quantidade de números Pares Múltiplos de 49 e 37 são: {index}")
