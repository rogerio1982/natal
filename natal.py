import random

numberList = ["@","#"]
#print("random item from list is: ", random.choice(numberList))

linhas = 20
tamanho = linhas * 2 - 10
espacos = (tamanho - 1) / 2
i = 1
 
while i <= linhas:
#print *
   print (""," " * (20 - i + 1), random.choice(numberList)  * (2 * i - 1))
   i = i + 1
    
#print ##
i=1
while i <= 20:
   print (""," " * (20 - i + 1), "##"  * (2 * i - 1))
   i = i + 1
   break
print ("Feliz Natal 2021!")
