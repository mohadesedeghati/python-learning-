weight =  float(input("How much is your weight?kg"))
height= float(input("How much is your height?m**2"))
BMI= weight/(height**2)
if 25<BMI<29.9:
    result="over weight"
elif 30<BMI<34.9:
    result="obesity"
elif 35<BMI<39.9:
    result= "extreme obesity"
print(BMI,result)