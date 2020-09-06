# Time Complexity : O(1)


def solution(x, y, D):
    if x == y:
        return 0

    distance = y - x
    lack_cnt = int(distance / D)
    lack_distance = distance % D
    if lack_distance == 0:
        cnt = lack_cnt
    else:
        cnt = lack_cnt + 1

    return cnt


def main():
    print(solution(1, 1, 10))
    print(solution(10, 85, 30))
    print(solution(10, 70, 30))
    print(solution(10, 10000000, 30))


if __name__ == "__main__":
    main()