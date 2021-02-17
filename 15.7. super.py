# 상속을 받을때 __init__을 통해서 받는 방법도 있지만 super라는 기능을 이용해 받는 방법도 있다

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

# 건물
class BuildingUnit(unit):
    def __init__(self, name, hp, location):
        # unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location

# 서플라이 디폿 : 건물, 1개 건물 = 8개 유닛 추가 생성 가능
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

