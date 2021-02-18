from random import *


class unit:
    def __init__(self, name, hp, speed):  # 여기서 __init__은 생성자이다
        self.name = name
        self.hp = hp
        self.speed = speed
        print("\n---{0} 유닛이 생성되엇습니다.---".format(self.name))  # 매개변수 self.name 혹시 파라미터 name 둘 다 상관없다
        if self.speed > 0:
            print("체력: {0}, 스피드: {1}".format(self.hp, self.speed))

    def move(self, location):
        print(("[지상 유닛 이동]"))
        print("{0} : {1} 방향으로 {2}의 속도로 이동합니다.".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 공격 유닛
class AttackUnit(unit):  # 상속하려는 클래스를 넣어줌
    def __init__(self, name, hp, damage, speed):
        # 유닛에서 만들어진 생성자를 호출
        unit.__init__(self, name, hp, speed)  # 유닛의 생성자인 name hp 호출
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))


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


'''chracter class'''


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # steam pack ability
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} steam pack mode on! \ncurrent hp : {1}".format(self.name, self.hp))
        else:
            print("{0} Not enough hp!")


class Tank(AttackUnit):
    # 시즈모드 : 탱그를 지상에 고정시켜, 더 높은 파월로 공격 가능. 이동 불가.
    seize_mode_developed = False # 시즈 모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 30, 7)
        self.seize_mode = False

    # seize mode
    def set_seize_mode(self):
        if Tank.seize_mode_developed == False:
            return

        if self.seize_mode == False:
            print("activating seize mode")
            self.damage *= 2
            self.seize_mode = True

        else:
            print("deactivating seize mode.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


class wraith(flyableAttackUnit):
    def __init__(self):
        flyableAttackUnit.__init__(self, "레이스", 80, 20, 5, 15)
        self.clocked = False  # 클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True:  # 클로킹 모드 해제
            print("{0} clocking mode deactivated".format(self.name))
            self.clocked = False
        else:
            print("{0} clocking mode activated".format(self.name))
            self.clocked = True


def game_start():
    print("starting the game")


def game_over():
    print("ending game")
    print("gg \nplayer has left the game")


# 게임 실행
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 4기 생성
w1 = wraith()
w2 = wraith()
w3 = wraith()
w4 = wraith()

# 유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)
attack_units.append(w2)
attack_units.append(w3)
attack_units.append(w4)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱그 시즈모드 개발
Tank.seize_mode_developed = True
print("sieze mode has been developed")

# 공격 모드 준비 (마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):  # isinstance를 통해 만들어진 객체가 클래스의 인스턴스인지 확인
        unit.stimpack()
    elif isinstance(unit, Tank):  # 탱크 유닛 인스턴스 확인
        unit.set_seize_mode()
    elif isinstance(unit, wraith):  # 레이스 유닛 인스턴스 확인
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20))  # 공격은 랜덤으로 받는다 (5 ~ 20)

# 게임 종료
game_over()
