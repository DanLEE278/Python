subway1 = 10
subway2 = 20
subway3 = 30

subway = [ subway1, subway2, subway3]
print(subway)

bus = ["고양이","강아지","수달"]
print(bus)

# 수달은 몇번째 칸에 타고 있는가?
print(bus.index("수달"))

# 만약 다음 정류장에서 호랑이가 탄다면
bus.append("호랑이")
print(bus)

# 만약 새로운 동물을 사이에 끼워 넣고 싶다면
bus.insert(1, "사자")
print(bus)

# 리스트에서 인덱스를 뺄 수도 있음
# 디폴트 값은 맨 마지막 인덱스를 리스트에서 뺌
print(bus.pop(1)) # 뺄 인덱스 설정
print(bus)

# 같은 동물이 몇 마리 있는지 셀때
bus.append("수달")
print(bus)
print(bus.count("수달"))

# 리스트 정렬
# 숫자인 경우는 인덱스 0 부터 작은 값들이 들어간다
# 단어인 경우에는 알파벳이나 한글 순으로 정렬
number_list = [5, 4, 7, 102, 3, 2]
number_list.sort()
print(number_list)

character_list = ["ㅃ", "ㄱ", "ㄷ", "ㅅ", "ㄴ", "ㅋ", "ㅅ"]
character_list.sort()
print(character_list)

# 순서 뒤집기
number_list.reverse()
print(number_list)

# 리스트 값들 모두 지우기
number_list.clear()
print(number_list)

# 다양한 값들을 리스트에 한번에 넣어 정리
mixed_list = ["조세호", 20, True]

# 리스트 확장
mixed_list.extend(bus)
print(mixed_list)