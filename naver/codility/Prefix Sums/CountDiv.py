# Time Complexity: O(1)
import sys


def solution(A, B, K):
    if A == 0:
        # 1을 더하는 이유 A=0 이기 때문, 0은 뭘로 나눠도 나머지가 0
        cnt = int(B / K) + 1
    else:
        cnt = int(B / K) - int((A-1) / K)

    return cnt

def main():
    print(solution(6, 11, 2))
    print(solution(0, 1, 1000))
    print(solution(1, sys.maxsize, 1000))


if __name__ == "__main__":
    main()