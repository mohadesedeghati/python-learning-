import random
list=[]
lenght=int(input("please enter the lengh of the list:  "))

for i in range (lenght):
    num= random.randint(1,40)
    list.append(num)
    print(list)


list.reverse()
print(list)