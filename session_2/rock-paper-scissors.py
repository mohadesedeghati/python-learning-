import random

for i in range(5):
    a= random.randint(1,3)
    C_score=0
    U_score=0
    if a==1:
        C_choice="rock"
    elif a==2:
        C_choice="paper"
    elif a==3:
        C_choice="scissors"
    
    u_choice= input("it's your turn to play: ")

    print("computer", C_choice)
    print("User", u_choice)

    if C_choice=="rock" and u_choice=="paper":
        U_score=+1
        print("U_score",U_score)
        continue
    elif C_choice=="paper" and u_choice=="rock":
        C_score=+1
        print("C_score",C_score)
        continue
    elif C_choice=="rock" and u_choice=="scissors":
         C_score=+1
         print("C_score",C_score)
         continue
    elif C_choice=="1cissors" and u_choice=="rock":
         U_score=+1
         print("U_score",U_score)
         continue
    elif C_choice=="scissors" and u_choice=="paper":
          C_score=+1
          print("C_score",C_score)
          continue
    elif C_choice=="paper" and u_choice=="scissors":
        U_score=+1
        print("U_score",U_score)
        continue

    elif U_score==2:
        print("user win")
        break
    elif C_score==2:
        print("user failed")
        break