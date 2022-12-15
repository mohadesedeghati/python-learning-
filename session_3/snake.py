n=int(input(" choose the lengh of your snake   "))
for i in range(n):
    
    if i %2==0:
        print("*", end="")
    else:
        print("#", end="")
 