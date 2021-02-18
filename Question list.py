'''
사용자로부터 입력받은 n번만큼의 행렬을 만들어 출력하세요
1보다 크고 10보다 작은 값을 입력하세요: 3
n의 값 = 3
'''

number = [1,2,3,4,5,6,7,8,9,10]

print("사용자로부터 입력받은 n번만큼의 행렬을 만들어 출력하세요")
input = int(input("1보다 크고 10보다 작은 값을 입력하세요: "))
index = 0
for i in range(int(len(number))//input):

    if i % 2 == 0:
        print(number[index:index+input])
        index += input
    else:
        copy = number[index:index+input]
        copy.reverse()
        print(copy)
        index += input
