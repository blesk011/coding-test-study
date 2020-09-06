# Time Complexity : O(n)

"""
최소, 최대 값을 구하는 방법
1. 비교할 값들을 지료형에 저장하고 반복문을 통해서 최소값을 구한다. - 쉽고 일반적으로 할수 있는 방법
특징: 저장되는 값의 개수가 많아질수록 시간복잡도가 증가
ex) for num in arr:
        # after calculation
        arr2.append(num2)

    min_num = min(arr)

2. 최소 값을 가지는 변수를 초기화하고 목적 계산을 하는 반복문에서 계산하자마자 값을 비교하여 최소 값을 업데이트하는 방법
특징: 계산하면서 값을 비교하기 때문에 공간복잡도에서 장점, 반복문 내부의 계산이 간단할수록 빠름, O(n)
ex) min = 0
    for num in arr:
        # after calculation
        if num2 < min:
            min = num2

    min_num = min
"""


def solution(A):
    front = 0
    back = sum(A)
    min_d = None

    for p in range(1, len(A)):
        front += A[p-1]
        back -= A[p-1]
        d = abs(front - back)
        if min_d is None:
            min_d = d
        else:
            min_d = min(min_d, d)

    return min_d


def main():
    print(solution([2, 3, 1, 5])) # (2, 9), (5, 6), (6, 5)
    print(solution([2, 4]))
    print(solution([2, 4, 345, 234, 12, 3, 3465, 675, 231, 85, 999]))


if __name__ == "__main__":
    main()