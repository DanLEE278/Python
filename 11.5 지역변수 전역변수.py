"""
변수라는건 함수 안에서 생성된 지역변수(local variable)이 있고
함수 밖에서 생성된 전역변수(global variable)이라는게 있다
통상적으로 프로그래밍을 할때 너무많은 전역변수를 쓰면 코트가 복잡해지고 좋지 않다
"""
price = 1500

# 지역 변수를 사용하는 경우
def spare_change(money):
    price = 2000 # 지역변수 price 사용
    change = money - price
    print("잔돈: {0}".format(change))

# 전역변수를 사용하고 싶을때
def spare_change1(money):
    global price # 전역변수 price를 불러옴
    change = money - price
    print("잔돈: {0}".format(change))

# 지역변수를 함수에 파라미터에 넣으면 더 깔끔하게 코딩 할 수 있다
# 결과값을 반환해서 전역 변수를 바꿀 수 있다
def spare_change2(price,money):
    change = money - price
    print("잔돈: {0}".format(change))
    return change

price = spare_change2(price, 50000)

# 지역변수
spare_change(5000)
spare_change2(1000,5000)

# 전역변수
spare_change1(4000)

