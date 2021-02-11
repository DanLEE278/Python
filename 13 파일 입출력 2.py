# 파일을 한 번에 모두 출력
print("\n한번에 다 읽어서 출력")
score_file = open("score.txt","r",encoding="utf8")
print(score_file.read()) # 내용을 전부 읽고 출력함
score_file.close()

# 파일을 한 줄 씩 출력
print("\n한줄씩 읽어 출력")
score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline(), end="") # 한 줄씩 읽고 출력
print(score_file.readline(), end="") # 한 줄씩 읽고 출력
print(score_file.readline(), end="") # 한 줄씩 읽고 출력
print(score_file.readline()) # 한 줄씩 읽고 출력
score_file.close()

# 파일을 while 반복문을 이용하여 출력
print("\nwhile문을 이용한 출력")
score_file = open("score.txt","r",encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line,end="")
score_file.close()

# 파일을 list를 이용하여 출력
print("\n\nlist를 이용한 출력:")
score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line,end="")
