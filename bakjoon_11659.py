# 문제 003 구간합 구하기 1
## 문제 : 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
## 입력 : 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다.
# 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.
## 출력 : 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.


# 내 풀이 - 오답
mylist = list(map(int, input().split(' ')))
n, m = mylist[0], mylist[1]
numlist = list(map(int, input().split(' ')))
sumlist = []

sumlist.append(numlist[0])

for index in range(1,n) :
    sumlist.append(sumlist[index-1] + numlist[index])

range1 = list(map(int, input().split(' ')))
range2 = list(map(int, input().split(' ')))
range3 = list(map(int, input().split(' ')))

def rangeSum(range) :
    if range[0] <= 1 :
        return sumlist[range[1] - 1]
    else :
        return sumlist[range[1] - 1] - sumlist[range[0] - 2]

print(rangeSum(range1))
print(rangeSum(range2))
print(rangeSum(range3))




# 교재 풀이
import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers :
    temp = temp + i
    prefix_sum.append(temp)

for i in range(quizNo) :
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])




# 내 풀이 수정 - 시간초과
n, m = map(int, input().split(' '))
numlist = list(map(int, input().split(' ')))
sumlist = [0]
temp = 0

for i in numlist :
    temp += i
    sumlist.append(temp)

def rangeSum(range) :
    return sumlist[range[1]] - sumlist[range[0] - 1]

for i in range(m) :
    s, e = map(int, input().split())
    print(sumlist[e] - sumlist[s-1])