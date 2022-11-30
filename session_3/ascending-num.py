a=int(input("please enter your first decision:  "))
b=int(input("please enter your second decision:  "))
c=int(input("please enter your third decision:  "))
d=int(input("please enter your fourth decision:   "))

array=[a,b,c,d]
if b>a and c>b and d>c:
    print("numbers are sorted properly")
    print(array)
    
else:
    print("numbers will be sorted properly now")
    array.sort()
    print(array)