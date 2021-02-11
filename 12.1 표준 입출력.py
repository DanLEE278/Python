# print("Python", "Java", "JavaScript", sep=" vs ") # 각각의 단어 사이에 무엇을 넣은건지 정해줌
#
# # 문장의 끝부분을 디폴트 값으로 다음 문장으로 넘어감
# # 하지만 end=""를 쓰면 바꿀 수 있음
# print("Python", "Java", "JavaScript", end="?") # 문장의 끝을 어떻게 끝낼건지 정해줌
#
# import sys
# print("Steven Gerrad", "Fernado Torres", file=sys.stdout)
# print("Steven Gerrad", "Fernado Torres", file=sys.stderr)

# 시험 성적
scores = {"수학":92, "영어":93, "국어":88}
for subject,score in scores.items():
    print(subject.ljust(8),str(score).rjust(4),sep=":") # ljust(8) 는 왼쪽으로 9칸 정렬 rjust(4) 는 오른쪽으로 4칸 정렬

# 은행 순번 대기표
for i in range(1,150):
    print("대기번호: " + str(i).zfill(3)) # 숫자 세자리 채워 넣음

# input을 받는 경우
name = input("이름이 어떻게 되세요?")
print(name + "님 만나서 반갑습니다")