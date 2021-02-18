'''
프로그램에서 의도적으로 에러를 발생시키는 경우
'''

try:
    print("한 자리 숫자 전용 계산기 입니다")
    num = []
    num.append(int(input("첫 번째 숫자를 입력하세요:\n ")))
    num.append(int(input("두 번째 숫자를 입력하세요:\n")))
    num.append(num[0]/num[1])

    if num[0] >= 10 or num[1] >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num[0], num[1], num[2]))

except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
