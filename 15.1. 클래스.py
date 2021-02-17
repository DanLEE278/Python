# 클래스는 일종의 틀과 비슷해서 비슷한거를 뽑아낼때 유용하게 쓰인다

# # 마린 : 공격 유닛, 군인
# name_marine = "마린"
# hp_marine = 50
# damage_marine = 5
#
# print("{0} 유닛이 생성되었습니다.".format(name_marine))
# print("체력 {0}, 공격력 {1}\n".format(hp_marine,damage_marine))
#
# # 탱크 : 공격 유닛,탱크, 시즈 모드
# name_tank = "탱크"
# hp_tank = 100
# damage_tank = 35
#
# print("{0} 유닛이 생성되었습니다.".format(name_tank))
# print("체력 {0}, 공격력 {1}\n".format(hp_tank,damage_tank))
#
# def attack(name, location, damage):
#     print("{0}이 {1} 방향으로 {2}의 데미지로 공격합니다.".format(name, location, damage))
#
# attack(name_marine, 1, damage_marine)

# 실제로 게임을 할때는 같은 유닛을 여러개 생성하기 떼문에 class를 이용해서 생산해주는게 편하다.

class unit:
    def __init__(self, name, hp, damage): # 여기서 __init__은 생성자이다
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되엇습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# class로 부터 만들어지는 유닛들을 객체라고 한다
# 여기서 marine, tank는 유닛 클래스의 instance 가 된다
marine1 = unit("마린", 40, 5) # 객체 1
marine2 = unit("마린", 40, 5) # 객체 2
tank = unit("탱크", 150, 35) # 객체 3

# class 를 사용하게 되면 추가로 변수를 넣어줄 수 있다
# 확장된 변수는 확장된 변수의 한에서 적용이 된다
wraith1 = unit("레이스", 80, 5)
print("유닛 이름 :, {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것
wraith2 = unit("레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("현재 {0}는 클로킹 상태입니다.".format(wraith2.name))

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)