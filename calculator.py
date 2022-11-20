import math
print("Enjoy fast calculating")

print ("+: sum")

print ("-: sub")

print ("*: mul")

print ("/: div")

print("**: power")

print("log")

print("sin")

print ("cos")

print ("please choose your operation")

op = input ()

if op == "+" or op =="-" or op =="*" or op =="/":
    a = float(input("please enter first number:"))
    b = float(input("please enter second number:"))

else:
    a = float(input("please enter first number"))

if op == "+":
    result = a + b

elif op == "-":
    result = a - b

elif op == "*":
    result = a * b

elif op == "/":
    if b == 0:
        result = "operation failed"
    else:
        result = a / b

elif op == "**":
    result = a ** b

elif op == "log":
    result= math.log(a)

elif op == "sin":
    result = math.sin(a)
    
elif op == "cos":
    result = math.cos(a)
 
print (result)