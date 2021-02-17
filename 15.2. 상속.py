# 2개의 클라스가 a, b가 있다고 가정할때 a 클라스를 b 클라스에 상속시킬 수 있다

class unit:
    def __init__(self, name, hp, damage): # 여기서 __init__은 생성자이다
        self.name = name
        self.hp = hp
        print("{0} 유닛이 생성되엇습니다.".format(self.name))
        print("체력 {0}, 체력 {1}".format(self.hp, self.hp))

# 공격 유닛
class AttackUnit(unit): # 상속하려는 클래스를 넣어줌
    def __init__(self, name, hp, damage):
        # 유닛에서 만들어진 생성자를 호출
        unit.__init__(self, name, hp) # 유닛의 생성자인 name hp 호출
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

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)