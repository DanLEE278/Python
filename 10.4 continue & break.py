# continue 와 break 는 반복문 안에서 사용이 가능하다
name = ["이유현", "김강민", "홍일표", "이정재", "이석현", "최민준"]


print("이씨 성만 골라내는 작업")
for item in name:
    if item[0] != "이":
        continue
    else:
        print(item)
    if item == "이정재":
        print("breaking loop")
        break