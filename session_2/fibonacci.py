import math
n=int(input("enter your ideal repeated times "))
f1=1
f2=0
if n==0:
    print("not defined")
elif n==1:
    print(f1)
elif n==2:
    fx=str(f1),str(f2)
    print(fx)
    
else:
    for i in range(n):
        fn=f1+f2
        print(fn)
        f1=f2
        f2=fn



