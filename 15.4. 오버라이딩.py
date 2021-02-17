# 다중 상속은 하나의 클래스가 두개 이상의 다른 클래스들을 받을때 사용
# 2개의 클라스가 a, b가 있다고 가정할때 a 클라스를 b 클라스에 상속시킬 수 있다

class unit:
    def __init__(self, name, hp, speed):  # 여기서 __init__은 생성자이다
        self.name = name
        self.hp = hp
        self.speed = speed
        print("\n---{0} 유닛이 생성되엇습니다.---".format(self.name))
        if self.speed > 0:
            print("체력: {0}, 스피드: {1}".format(self.hp, self.speed))

    def move(self, location):
        print(("[지상 유닛 이동]"))
        print("{0} : {1} 방향으로 {2}의 속도로 이동합니다.".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(unit):  # 상속하려는 클래스를 넣어줌
    def __init__(self, name, hp, damage, speed):
        # 유닛에서 만들어진 생성자를 호출
        unit.__init__(self, name, hp, speed)  # 유닛의 생성자인 name hp 호출
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 날 수 있는 유닛
class flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 유닛 공격 클래스
class flyableAttackUnit(AttackUnit, flyable):
    def __init__(self, name, hp, damage, speed, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, speed)
        flyable.__init__(self, flying_speed)
        print("체력: {0}, 스피드: {1}".format(self.hp, self.flying_speed))

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 발키리 생성
valkyrie = flyableAttackUnit("발키리", 100, 10, 13, 15) # 클래스를 호출할때 self 를 모두 넣어줌
valkyrie.fly(valkyrie.name, "3시") #
valkyrie.attack("3시")

# 벌쳐 생성
valture = AttackUnit("Vulture", 50, 9, 100)
valture.move("3시 방향")

# 배틀쿠루저 생성
battleCrusier = flyableAttackUnit("battle crusier", 200, 30, 0, 5)
battleCrusier.fly("battle crusier", "5시") # 벌쳐와는 다르게 배틀쿠루져는 fly라는 함수를 통해서 움직여야함
# 이거를 move 라는 함수로 통일 시키려면 class flyableAttackUnit에 move라는 함수를 추가해준다
battleCrusier.move("5시")