'''
가변인자는 함수에 들어가는 파라미터의 개수가 확실하지 않을때
시간을 단축해주기위해 쓴다
'''

# 가변인자를 쓰지 않는 경우의 예시
def profile(name, age, food1, food2, food3, food4):
    print("이름: {0}\t 나이: {1}\t 좋아하는 음식:".format(name,age), end=" ") # end = " "로 설정해주므로써 줄바꿈 없이 공백으로 끝남
    print(food1,food2,food3,food4)

profile("Steven Gerrad", 28, "Mc_donald", "archies", "pizz-co", "red chilli" )

# 살라는 만약에 좋아하는 음식이 하나 밖에 없다면 나머지는 빈칸으로 채워야한다
# 이럴 결우 가변인자를 사용하는 것이 편리하다
profile("Salah",29,"Mc donalds","","","")

# 가변인자를 사용할 경우 예시
def profile2(name,age,*food):
    print("이름: {0} 나이: {1} 좋아하는 음식: ".format(name, age), end=" ")
    for item in food:
        print("{0}".format(item), end = " ")

profile2("Dan",24,"five guys", "Archies", "Red chilli")