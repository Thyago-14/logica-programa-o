n1 = float(input("Digite o primeiro número: "))

n2 = float(input("Digite o segundo número: "))

operação = input("escolher a operação (+,-,*,/):")


#Se a operação for igual a "+", então:
if operação == '+':
  # a variável resultado recebe (n1 + n2)
  resultado = n1 + n2
#Senão se a operação for igual a "-", então:
elif operação == '-':
   # a variável resultado recebe (n1 - n2)
   resultado = n1 - n2
#Senão se a operação for igual a "*", então:
elif operação == '*':
  # a variável resultado recebe (n1 * n2)
  resultado = n1 * n2
#Senão se a operação for igual a "/", então:
elif operação == '/':
  # a variável resultado recebe (n1 / n2)
  resultado = n1 / n2
#Senão:
else:
   # a variavel resultado recebe o texto "operação inválida"
   resultado ="operação invalida"


#imprimir a variável resultado
print(f"o resultado da operação é: {resultado}")



