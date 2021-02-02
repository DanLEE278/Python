# tuple은 리스트와 비슷한데 리스트처럼 내용을 추가하거나 뺄 수 없다
# 하지만 연산 처리 속도가 list보다 빠르다
# 정리하면 튜플은 고정된 값에만 쓸 수 있다

squad = ("Torres", "Gerrad", "Henderson")
print(squad[0])

(name, age, position) = ("Torres", 20, "striker")
print(name,age, position)