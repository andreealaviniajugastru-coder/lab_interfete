 #ex 1
picture = [
 [0,0,0,1,0,0,0],
 [0,0,1,1,1,0,0],
 [0,1,1,1,1,1,0],
 [1,1,1,1,1,1,1],
 [0,0,0,1,0,0,0],
 [0,0,0,1,0,0,0]]
for row in picture:
     for x in row:
          if x  ==1:
              print("*", end="")
          else:
              print(" ", end="")
     print()

#ex2
# while True:
#     nota=float(input("introdu nota (1-10): "))
#     if nota < 1 or nota > 10:
#         print("nota invalida")
#         continue
#     if 9 <= nota <= 10:
#         print("excelent")
#     elif 7<= nota <=8:
#         print("bine")
#     elif 5 <= nota <=6:
#         print("suficient")
#     else:
#         print("reexaminare")
#     break

#ex3
import random
numar= random.randint(1,50)
while True:
     guess = int(input("ghiceste nr(1-50: "))
     if guess < numar:
         print("nr este mai mare")
     elif guess > numar:
         print("nr este mai mic")
     else:
         print("felicitari! ai ghicit")
         break

#ex4
