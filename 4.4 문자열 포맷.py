# 방법 1
print("나는 %d 살 입니다." % 19) # 숫자를 받음
print("저는 %s를 좋아해요" % "강아지") # 스트링을 받음
print("Apple starts with %c" %"A") # 하나의 문자를 받음
print("저는 %s 색과 숫자 %d를 좋아해요" %("빨간",20))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

# 방법 3
print("나는 {age}살이며 저는 {color}색을 좋아합니다".format(age=19, color="red"))

# 방법 4 (python version>3.6)
age = 20
color = "Red"
print(f"나는 {age}살이며 저는 {color}색을 좋아합니다.")