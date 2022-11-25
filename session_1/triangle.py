a= float(input("please insert the first side"))
b= float (input("please insert the second side"))
c= float (input("please insert the third side"))

if a+b>c and a+c>b and b+c>a:
    result="accepted"
else:
    result = "not accepted"
print(result)