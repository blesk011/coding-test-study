# Time Complexity : O(N)


"""
마지막에만 N 보다 작은 수를 count 해야함.
"""


def solution(N, A):

    arr = [0] * N
    c_max_cnt = 0
    last_max_cnt = 0

    # 전체 배열 순회
    for i, num in enumerate(A):
        if num < N+1:
            if arr[num-1] > last_max_cnt:
                arr[num-1] += 1
            else:
                arr[num-1] = last_max_cnt + 1

            if arr[num-1] > c_max_cnt:
                c_max_cnt = arr[num-1]
        # N+1과 동일한 값이면, 현재까지 최대로 나온 숫자의 횟수로 바꿔줌
        elif num == N+1:
            last_max_cnt = c_max_cnt

    for i, cnt in enumerate(arr):
        if cnt < last_max_cnt:
            arr[i] = last_max_cnt

    return arr


def main():
    print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
    # print(solution(5, [1, 1, 1, 1, 1, 1, 1]))
    # print(solution(1, [2]))
    print(solution(2, [3, 3, 1]))


if __name__ == "__main__":
    main()