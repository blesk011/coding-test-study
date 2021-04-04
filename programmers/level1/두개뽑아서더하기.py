def solution(numbers):
    res = []
    """
    내 풀이
        numbers 배열의 인덱스를 비교해서 다른 경우에만 덧셈을 함
    Approach 2
        현재 인덱스 이후의 인덱스끼리만 덧셈을 진행
        i=0 일때 j=1, 2, 3, 4 진행
        i=1 일때 j=2, 3, 4 진행
        
        * 연산 횟수
        n^2 ==> n^2 / 2 (절반으로 줄어듦)
    """

    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers):
            if i != j:
                res.append(num1 + num2)

    answer = sorted(list(set(res)))
    return answer


if __name__ == "__main__":
    print(solution([2,1,3,4,1]))
    print(solution([5,0,2,7]))
