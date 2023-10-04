# 선택 정렬과 기본 정렬 라이브러리의 수행 시간 비교

import time
from random import randint

array = []
for _ in range(10000) :
    array.append(randint(1, 100))


start_time = time.time()

# 선택정렬 코드
for i in range(len(array)) :
    min_index = i
    for j in range(i + 1, len(array)) :
        if array[min_index] > array[j] :
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 스와프

end_time = time.time()
print('선택정렬 소요시간 : ', end_time - start_time)


array = []
for _ in range(10000) :
    array.append(randint(1, 100))

start_time = time.time()

# 기본 정렬 라이브러리
array.sort()

end_time = time.time()
print('기본 정렬 소요시간 : ', end_time - start_time)