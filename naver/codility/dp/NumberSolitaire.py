# Time Complexity: O(Sqrt(N))


def solution(A):
    print(A)
    S = [1, -1]
    arr = [[0 for _ in range(len(A))] for _ in range(2)]
    arr[0][0] = A[0] * S[0]
    arr[1][0] = A[0] * S[1]

    for i in range(1, len(A)):
        num1 = arr[0][i-1] + A[i]*S[0]
        num2 = arr[0][i-1] + A[i]*S[1]
        num3 = arr[1][i - 1] + A[i] * S[0]
        num4 = arr[1][i - 1] + A[i] * S[1]

        if abs(num1) < abs(num2):
            arr[0][i] = num1
        else:
            arr[0][i] = num2

        if abs(num3) < abs(num4):
            arr[0][i] = num3
        else:
            arr[0][i] = num4

    print(arr)

    if abs(arr[0][len(A)-1]) >= abs(arr[1][len(A)-1]):
        return abs(arr[1][len(A)-1])
    else:
        return abs(arr[0][len(A) - 1])


def main():
    print(solution([1, 5, 2, -2]))


if __name__ == "__main__":
    main()
