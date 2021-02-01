
# 1st example
name = "Dan"
hieght  = 178

if hieght > 177:
    height = "sexy"
else:
    height = "cute"
print("Hi my name is",name, "\nI am", height) # 1st way of printing


# 2nd example
''' 여러 문자에 대해 주석 처리하고 싶을떼'''

name = "Jude"
age = 75
adult = age > 21
print("Hi I'm", name, "\nAm I an adult?", adult) # 1st way if printing
print("Hi I'm " + name + "my age is " + str(age) + "\nIs he an adult? " + str(adult)) # convert integer/boolean into string to print