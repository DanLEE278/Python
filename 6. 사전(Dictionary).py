# 사전이라 불리는 이유
# 사전을 찾아보면 단어와 설명으로 이루어져있다
# 예를들면 "파이썬: 코딩 언어의 한 종류" 와 같이
# 그 뜻과 의미를 갖고 있는거를 dictionary 라고 부른다
squad = {8:"Steven gerrad", 9:'Fernado Torres'}

print(squad[8])
print(squad[9])
#print(squad[10]) # squad에 없는 값을 출력하려고 하면 에러 발생

print(squad.get(10)) # 이럴때 squad.get() 함수를 이용하면 dictionary에 포함되지 않은 key여도 None 반환
print(squad.get(11, "비어 있음 사용 가능"))

print(8 in squad) # true
print(10 in squad) # false

dictionary = {"무한도전":"유재석","1박 2일":"강호동"}
print(dictionary["무한도전"])

# dictionary 안에 값들을 바꿔줄때
dictionary["무한도전"] = "신동엽"
dictionary["신서유기"] = "이수근"
print(dictionary)

# dictionary 안 값들을 지우는 법
del dictionary["1박 2일"]
print(dictionary)

# key 값들만 출력
print(dictionary.keys())

# value 값들만 출력
print(dictionary.values())

# key vlue 쌍으로 출력
print(dictionary.items())

# 방송 프로그램 모두 폐지
dictionary.clear()
print(dictionary)