# Time Complexity: O(1)


def solution(S, P, Q):
    if_dict = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    S = [int(if_dict[s]) for s in S]
    arr = []

    for p, q in zip(P, Q):
        part_num = S[p:q+1]

        part_min = min(part_num)
        arr.append(part_min)

    return arr


def main():
    print(solution('CAGCCTA', [2, 5, 6], [4, 5, 6]))
    print(solution('C', [0], [0]))
    print(solution('CAGCCTACAGCCTACAGCCTACAGCCTACAGCCTACAGCCTA', [2, 4, 5, 6, 7, 12, 20, 31], [3, 5, 8, 9, 10, 15, 21, 32]))


if __name__ == "__main__":
    main()