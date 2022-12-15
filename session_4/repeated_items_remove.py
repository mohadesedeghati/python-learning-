num=[]
Main_num=[]
while True:
    user=input("please enter number or choose 0 to finish:  ")
    if user== 0:
        break
    else:
        num.append(user)
        print(num, end=" ")

    for user in num:
        if user not in Main_num:
            Main_num.append(user)
            print(Main_num, end=" ")

