sentence = "python is amazing"

print(sentence.lower()) # 모든 문자들을 소문자로 바꿈

print(sentence.upper()) # 모든 문자들을 대문자로 바꿈

sentence[0].upper() # 지정된 위치만 대문자로 바꿈

print(sentence[0].isupper()) # 그 위치의 문자가 대문자인지 소문자인지 진위 판별

print(len(sentence)) # 문장의 길이 반환

print(sentence.replace("python", "java")) # 지정된 문자를 바꿔줌

index = sentence.index("n") # 지정된 문자가 몇번째 인덱스에 있는지 알려줌
print(index)
index = sentence.index("n",index+1) # index+1 이후의 문자서부터 탐색 시작
print(index)

print(sentence.find("amazing")) # find 함수도 index랑 비슷하지만 find 는 문장에 포함되지 않는 단어를 찾으면 -1 을 반환 index 함수는 error 나면서 중단

print(sentence.count("n")) # n 이 총 몇번 등장하는지 알려줌