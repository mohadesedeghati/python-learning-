import math
n = 0
sum= 0
while True:
    score=input("please enter your score or choose to exit:  ")

    if score == "exit":
        print("you choose to exit the program")
        break
    else:
        score= float(score)
        n= n+1
        sum= sum + score
        average= sum/n
        print (average)

