import random

num = random.randint (1 , 6)
guess = 1

while guess <= 6:
    g = int(input("Enter Number 1 - 6 : "))
    if g == num:
         print(f" You Won - {num}")
         break
    guess += 1

else:
     print(f"You Lose {num}")


