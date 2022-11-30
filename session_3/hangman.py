import random

words_source=["sky","tree","river","lake","mountain","hill"]

user_error=0

correct_guess=[]
wrong_guess=[]

choice=random.randint(0, len(words_source)-1)

word=words_source[choice]


while user_error<6:
    for i in range(len(word)):
        if word [i] in correct_guess:
            print(word[i], end=" ")
        else:
            print("-", end=" ") 
    if len(word)== len(correct_guess):
        print("congrats!! you win")
        break

    player_guess=input("It's time to guess: ")

    player_guess=player_guess.lower()
    
    if len(player_guess)==1:
        if player_guess in word:
            correct_guess.append(player_guess)
            print("yes")
        else:
            wrong_guess.append(player_guess)
            user_error += 1
            print("No!")
    else:
        print("use only one charachter")