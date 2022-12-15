import math
num=int(input("enter number:  "))

f=1

while num>0:
    if num%f !=0:
        print("No")
        break
    elif num%f ==0:
        num/f
        if num/f==1:
            print("yes")
            break


