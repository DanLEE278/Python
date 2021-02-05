'''
함수를 만들때 키워드 값을 설정해 줄 수 있다
축구팀의 스쿼드에 관한 함수를 만들어준다고 가정했을때
함수를 호출할때 키워드를 지정하여 호출 할 수 있다
'''

def football_squad(name, age, height): # 이름은 다 다르지만 나이와 키가 다 똑같다고 가정할때
    print("이름: {0} 나이: {1} 키: {2}".format(name,age,height))

football_squad(name = "Steven Gerrad",age=28, height=182)
football_squad(age = 29, name = "Jamie Carragher", height = 185)