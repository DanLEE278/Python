# for loop는 특정값을 반복해서 할 수 있게 해줌

# int 를 item으로 받는 경우
for waiting_no in [0,1,2,3,4]:
    print("waiting number: {}".format(waiting_no))

# 위의 방법보다 더 편한 방법
for waiting_no in range(5):
    print("waiting number {0}: ".format(waiting_no))

# string 을 item으로 받는 경우
actor_list = ["하정우", "이정재", "정우성"]
for actor in actor_list:
    print("안녕하세요 저는 {} 입니다".format(actor))

# 한줄짜리 for 문
# example 1
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students] # 리스트를 바꿈
print(students)

# example 2
# 문자의 길이를 정수 값으로 변환할때
students = ["Lauv", "Steven Gerrad", "Fernando Torres"]
print(students)
students_num = [len(name) for name in students]
print(students_num)
students_capital = [name.upper() for name in students]
print(students_capital)