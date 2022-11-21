name= input("please enter your name")
family= input("please enter your last name")
c= float(input("please enter your first score"))
d= float(input("please enter your second score"))
e= float(input("please enter your third score"))
average= (c+d+e)/3
if average>=17:
    result="great"
elif 12<=average<=17:
    result="normal"
elif average<12:
    result = "fail"
print(name, family, result)


