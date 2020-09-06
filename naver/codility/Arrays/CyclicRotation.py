def solution(A, K):
    arr = A
    if len(arr) == 0:
        return []

    for _ in range(K):
        new_arr = []
        temp = arr[-1]
        remain_arr = arr[:-1]

        new_arr.append(temp)
        new_arr += remain_arr
        arr = new_arr

    return arr


def main():
    A = [3, 8, 9, 7, 6]
    print(solution(A, 3))
    print("===============")
    print(solution([0, 0, 0], 1))
    print("===============")
    print(solution([1, 2, 3, 4], 4))
    print("===============")
    print(solution([], 4))
    print("===============")
    '''
    print(solution(9))
    print("===============")
    print(solution(529))
    print("===============")
    print(solution(20))
    print("===============")
    print(solution(32))
    print("===============")
    print(solution(1041))
    print("===============")
    '''

if __name__ == "__main__":
    main()
