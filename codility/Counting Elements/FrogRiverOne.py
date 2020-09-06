# Time Complexity : O(N)


def solution(X, A):
    target_position = X
    exist_check = [False for _ in range(target_position)]
    cnt = 0

    '''
    1. 개구리가 절대 다른 쪽 강둑으로 이동 못하는 경우
        X=5 일 때, [1, 2, 3, 4, 5] 중에 하나라도 존재하지 않으면 절대 못감
    2. 이동할 수 있는 경우
        X=5 일 때, [1, 2, 3, 4, 5]가 모두 존재하는 경우
    '''

    # if target_position not in A:
    #     return -1
    '''
    조건을 충족했는지 표시할 리스트 자료형 변수를 이용하여
    확인하고 이미 확인한것은 넘기고(중복 제거) 조건의 개수를 확인하여 
    모든 조건을 충족하면 종료
    '''
    for i, position in enumerate(A):
        if position <= target_position:
            if exist_check[position-1]:
                continue
            exist_check[position-1] = True
            cnt += 1
        if cnt == X:
            return i

    return -1


def main():
    print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
    # print(solution(5, [1, 3, 1, 4, 2, 3, 1, 2, 4]))


if __name__ == "__main__":
    main()