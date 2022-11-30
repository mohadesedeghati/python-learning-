import random
first_num=int(input("plz enter your lower bound:  "))
last_num=int(input("plz enter your higher bound:   "))
n=int(input("please choose your ideal range:  "))

list=[]

for i in range(n):
    num=random.randint(first_num,last_num)
    list.append(num)
print(list)