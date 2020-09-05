def solution(N):
    gaps = []
    b_N = format(N, 'b')
    print(b_N)
    # print(type(b_N))
    if len(b_N) == 1:
        return 0

    one_idxs = [idx for idx in range(len(b_N)) if int(b_N[idx]) == 1]
    if len(one_idxs) == 1:
        return 0
    print(one_idxs)
    for i in range(len(one_idxs)):
        if i == len(one_idxs) - 1:
            break
        gap = int(one_idxs[i+1]) - int(one_idxs[i]) - 1
        gaps.append(gap)

    max_gap = max(gaps)
    return max_gap


def main():
    N = 2147483647
    # print(solution(N))

    print(solution(1))
    print("===============")
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


if __name__ == "__main__":
    main()