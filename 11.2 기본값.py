'''
함수를 만들때 기본 값을 설정해 줄 수 있다
축구팀의 스쿼드에 관한 함수를 만들어준다고 가정했을때
선수들의 공통된 값이 있다고 가정하면 파라미터에 기본 값을 지정하는게 유용함
'''

def football_squad(name, age=17, hieght=178): # 이름은 다 다르지만 나이와 키가 다 똑같다고 가정할때
    print("이름: {0} 나이: {1} 키: {2}".format(name,age,hieght))

football_squad("Steven Gerrad")
football_squad("Jamie Carragher")