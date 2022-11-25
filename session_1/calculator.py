import math
print("Enjoy fast calculating")

print ("+: sum")

print ("-: sub")

print ("*: mul")

print ("/: div")

print("**: power")

print ("sqrt")

print("log")

print("sin")

print ("cos")

print ("tan")

print ("cot")

print ("factorial")

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

elif op == "sqrt":
    if a>0:
        result = math.sqrt(a) 
    if a<0:
        result ="not defined"

elif op == "log":
    result= math.log(a)

elif op == "sin":
    a= a*0.0174
    result = math.sin(a)
    
elif op == "cos":
    a= a*0.0174
    result = math.cos(a)
      
elif op == "tan":
    a= a*0.0174
    result = math.tan(a)
elif op== "cot":
    a= a*0.0174
    result= math.cot(a)
 
print (result)