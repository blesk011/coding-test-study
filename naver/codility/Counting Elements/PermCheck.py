# Time Complexity: O(N) or O(N * logN)


def solution(A):
    i_max = max(A)
    i_len = len(set(A))

    """
    if max != len:
        return 0
    """

    t_sum = (i_max * (i_max-1)) / 2
    i_sum = sum(set(A))
    if t_sum == i_sum:
        return 1




def main():
    print(solution([4, 1, 3, 2]))               # 1
    print(solution([4, 1, 3]))                  # 0
    print(solution([2, 3, 4]))                  # 1


if __name__ == "__main__":
    main()