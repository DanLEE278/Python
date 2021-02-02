def open_account():
    print("새로운 계좌가 생성되었습니다")

def deposite(balance, money): # 입금
    print("{0}원이 입금이 완료되었습니다. 현재 통장 잔액은 총 {1}원 입니다.".format(money, balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money:
        print("{0}원이 출금되었습니다\n남은 금액은 {1}원".format(money, balance-money))
    else:
        print("금액이 부족하여 출금이 불가능합니다\n현재 계좌 잔액은 {0}원 입니다".format(balance))

# 위의 경우와 똑같은데 return으로 값을 받고 함수 밖에서 출력하는 경우
def withdraw2(balance, money): # 출금
    if balance >= money:
        print("{0}원이 출금되었습니다".format(money))
        return balance-money
    else:
        print("금액이 부족하여 출금이 불가능합니다\n현재 계좌 잔액은 {0}원 입니다".format(balance))
        return balance

# 두개 이상의 값을 return하는 경우
def withdraw3(balance, money):
    commission_fee = 100
    if balance <= money:
        print("잔고에 돈이 부족합니다")
    return commission_fee, balance - money - commission_fee


open_account()
deposite(1000000, 550000)
withdraw(5000,7000)
withdraw2(5000,4000)
commission_fee, balance = withdraw3(10000,1500)
print("수수료: {0}\n통장잔고: {1}".format(commission_fee,balance))