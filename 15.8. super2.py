# super 기능은 다중상속을 받을때 문제점이 생긴다
class cat():
    def __init__(self):
        print("cat 생성자")

class dog():
    def __init__(self):
        print("dog 생성자")

class animal(cat, dog):
    def __init__(self):
        super().__init__()

class animal2(cat, dog):
    def __init__(self):
        cat.__init__(self)
        dog.__init__(self)

# super로 다중상속을 받을때는
# 다음과 같은 경우는 cat 생성자만 만들어진다
# 뒤에 나오는 dog는 호출되지 않으니 조심
animal = animal()
print("\n")

# 다중상속시에 모든 클래스를 생성하고 싶다면 super를 쓰지 않는게 낫다
# 다음 예시는 spuer를 쓰지 않는 경우
animal2 = animal2()