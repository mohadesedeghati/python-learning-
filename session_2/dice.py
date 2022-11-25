import random
print("Drop the dice")
Dice=random.randint(1,7)
for i in range(10):
    move=input("choose to start or exit: ")
    if move=="start":
        print(Dice)
        if Dice==6:
           print("you've win another move")
           price=random.randint(1,7)
           print(price)
           continue
    elif move=="exit":
        print("try again")
    break