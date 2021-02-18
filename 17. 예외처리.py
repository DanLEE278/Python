'''
예외처리는 프로그램을 돌리때 발생할 수 있을 만한 에러에 대한 조치를 취해준다
'''

try:
    print("나눗셈 전용 계산기 입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력해 주세요: "))) # str 값으로 받는다
    nums.append(int(input("두 번째 숫자를 입력해 주세요: "))) # str 값으로 받는다
    nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

# Value Error 처리
except ValueError:
    print("에러가 발생하였습니다. 잘못된 값을 입력하였습니다.")

# ZeroDivisionError 처리
except ZeroDivisionError as err:
    print(err)

# 그 외에 모든 에러 처리하는 법
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)