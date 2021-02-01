
# 일반 연산
print(2**3) # 2^3 =8
print(5%3) # 5 나누기 3 나머지 = 1
print(11%3) # 10 나누기 3 나머지 = 2
print(5//3) # 5 나누기 3 의 몫 = 1

# boolean 연산
print(4>3)
print(4>=6)
print(4==8)
print(4 != 8)

# and or not
print(not(4 != 5)) # 반대의 경우
print((4>3) and (5>7)) # 모두 True일 경우
print((4>3) & (5>7)) # 위의 경우와 같음
print((4>3) or (5<10)) # 둘 중 하나만 True 일 경우
print((4>3) | (5<3)) # 위와 같은 경우

# 그외 연산자
print(abs(-5))
print(pow(4,2)) # 4^2
print(max(5,12))
print(min(5,12))
print(round(3.14))
print(round(4.99))

from math import *
print(floor(4.99))
print(ceil(3.14))
print(sqrt(16))