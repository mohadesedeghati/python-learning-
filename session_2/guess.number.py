import random
computer_num= random.randint(10,50)
guess_number=0

while True:
    operator_guess= int(input("it's time to guess: "))

    if computer_num>operator_guess:
        print("guess higher")
        guess_number= guess_number+1

    elif computer_num<operator_guess:
        print("guess lower")
        guess_number= guess_number+1

    elif computer_num==operator_guess:
        print("Well done, you win!")
        guess_number= guess_number+1
        print("you have guessed",guess_number,"times")
        break