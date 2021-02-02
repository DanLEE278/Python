# while

customer = ["이정재", "이철웅", "제이","인하","솔범"]
index = 5

while index >= 1:
    print("{0}님 주문하신 커피가 준비됐습니다, 오늘 남은 커피 재고량: {1}회분".format(customer[index-1],index))
    index -= 1
    if index == 0:
        print("모든 커피가 소진되었습니다")

# 무한 루프
'''
while True:
    print("Infinity loop")
'''

# input을 받는 경우
customer_name = "이정재"
input_name = ""
index = 0

while input_name != customer_name:
    if index == 0:
        print("{0} 손님 주문하신 아메리카노가 나왔습니다.".format(customer_name))
        input_name = input("손님 이름이 어떻게 되세요?\n")
        index += 1
    if index != 0:
        print("{0} 손님 안계시나요?".format(customer_name))
        input_name = input("손님 이름이 어떻게 되세요?\n")
    if input_name != customer_name:
        print("죄송합니다 다른 고객님 커피입니다 손님")
