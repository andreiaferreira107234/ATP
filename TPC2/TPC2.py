#Pessoa adivinha
import random


tentativas = 0
min=0
max=100
x= random.randint(min, max)
y=int(input("Tenta adivinhar o número em que estou a pensar"))

while y !=x and tentativas <=  10:
 if y > x:
    y=int(input("Tenta outra vez. Uma dica: o número é menor"))
    tentativas = tentativas + 1
 elif y < x:
    y=int(input("Tenta outra vez.Uma dica: é maior"))
    tentativas = tentativas + 1
  
num = tentativas
if x==y:
 print(f"Parabéns!Acertaste em {num} tentativas")
else:
   print(("Esgostaste as tuas tentativas womp womp"))

#computador a adivinhar
from random import randint
num1=int(input("escolha um número de 0 a 100"))
min=0
max=100
num2=int(randint(min,max))
tentativas1 = 1
while num1!=num2:
  if num2<num1:
     print("o número que pensei é maior")
     min=min+1
  else:
      print("o número em que pensei é menor")
      max=max-1
  num2=int(randint(min,max))
  tentativas1=tentativas1 + 1    
resultado="Acertou com "+ str(tentativas1) +"tentativas"
print(resultado)