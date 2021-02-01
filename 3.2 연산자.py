from random import *

print(random()) # 0 ~ 1 까지 무작위 숫자
print(random()*10) # 0 ~ 10 까지 무작위 숫자
print(int(random()*10)) # 0 ~ 10까지의 임의의 정수 생성

print(int(random()*10)+1) # 1 ~ 11까지의 임의의 정수 생성
print(randrange(1,45)) # 1 부터 45미만의 값 생성
print(randint(1,45))

# quizz

date = randint(4,28)
print("This month offline study date: " + str(date))