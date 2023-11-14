import sys

dp = [0] * 1001

def solution(N):
    dp[1] = 1
    dp[2] = 2

    for n in range(3, N+1):
        dp[n] = int(dp[n-1] + dp[n-2]) % 10007

    return dp[N]
    

def read_N() -> int:
    N = int(sys.stdin.readline())
    return N


def run():
    N = read_N()
    print(solution(N))


if __name__ == "__main__":
    run()