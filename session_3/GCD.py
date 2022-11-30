print(" this program will calculate the Greator common divisor of chosen parameteres.")

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
        print("the calculated GCD is : ", GCD)

