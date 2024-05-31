print("привіт!")
from random import randint
num = randint(1,100)
user = int(input("вгадай число "))
i = 0
while num != user:
    print("не правильно")
    if user > num:
        print("Число менше")
    if user < num:
        print("Число більше")
    user = int(input("Вгадай число "))
    i += 1
print ("Вітаю!!! Це було число "+ str(user) + " Кількість спроб = "+ str(i))