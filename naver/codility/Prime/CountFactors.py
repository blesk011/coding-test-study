# Time Complexity: O(Sqrt(N))


def solution(N):
    cnt = 0
    i = 1

    while (int(i * i) < N):
        if int(N % i) == 0:
            cnt += 2
        i += 1

    if i * i == N:
        cnt += 1

    return cnt


def main():
    print(solution(24))
    print(solution(1))


if __name__ == "__main__":
    main()
