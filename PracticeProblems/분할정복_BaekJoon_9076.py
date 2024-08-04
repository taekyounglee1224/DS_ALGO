def swap(A,i,j):

    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def quicksort(A, start, end):
    if start >= end:
        return

    # 피벗 선택 (중간값)
    mid = (start + end) // 2
    pivot = A[mid]
    
    left, right = start, end

    while left <= right:
        while A[left] < pivot:
            left += 1
        while A[right] > pivot:
            right -= 1
        
        if left <= right:
            swap(A, left, right)
            left += 1
            right -= 1

    quicksort(A, start, right)
    quicksort(A, left, end)

def total_score(scores):
    # 퀵소트를 이용해 점수 정렬
    quicksort(scores, 0, len(scores) - 1)
    # 중간 세 점수 합산
    if scores[3] - scores[1] >= 4:  # 최대 점수와 최소 점수의 차이 검증
        return "KIN"
    else:
        return sum(scores[1:4])


import sys
input = sys.stdin.read
data = input().splitlines()


T = int(data[0])
results = []
    
for i in range(1, T + 1):
    scores = list(map(int, data[i].split()))
    result = total_score(scores)
    results.append(result)

for result in results:
    print(result)


