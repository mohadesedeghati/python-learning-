print(" this program will calculate the least common multiple")
while True:
    num1=int(input("please enter the first number:  "))
    num2=int(input("please enter the second number:  "))
    if num1>num2:
        n= num2
    else:
        n=num1
    for i in range(1,n+1):
        if num1 %i==0 and num2 % i ==0:
            GCD= i
        LCM=int((num1*num2)/GCD)
        print("the calculated LCM is : ", LCM)