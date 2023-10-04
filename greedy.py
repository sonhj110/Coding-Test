import time

# 그리디 알고리즘, 탐욕법 
# 손님이 돈 n원을 냈을때 거슬러줘야 할 동전의 최소 개수 구하기

n = 1260
count = 0

coin_types = [500, 100, 50, 10]   # 단위가 큰 동전이 항상 작은 동전의 배수이기 때문에 가능한 코드

for coin in coin_types :   # 시간 복잡도는 coin_types의 개수에 달림 
    count += n // coin 
    n %= coin   # n = n % coin 

print(count)


# 문제 1 큰 수의 법칙
## n개의 자연수로 구성된 배열이 있을때 총 m번 더하고 가장 큰 수를 만들어라
## 이때 같은 수를 연속으로 최대 k번 더할 수 있다
## 배열 안에 같은 수가 두번 이상 들어간 것은 다른 수로 간주한다 

## 수를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

start_time = time.time()

## 가장 큰 수랑 두번째로 큰 수 구하기 
data.sort()
first = data[-1]
second = data[-2]

result = 0


# 내 풀이
while True :
    if m == 0 :
        break
    for i in range(k) :
        result += first
        m -= 1
        if m == 0 :
            break
    result += second
    m -= 1

print(result)

end_time = time.time()
print('소요시간 : ', end_time - start_time)


# 정답
while True :
    for i in range(k) :
        if m == 0 :
            break
        result += first
        m -= 1
    if m == 0 :
        break
    result += second
    m -= 1
    print(m)





