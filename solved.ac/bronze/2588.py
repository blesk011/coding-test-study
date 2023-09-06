import math


def solution(num1, num2):
    # 385 -> 5, 8, 3
    '''
    i=0, 10^0 = 1
    i=1, 10^1 = 10
    i=2, 10^2 = 100
    
    '''
    values = list()
    total = 0
    for i, digit in enumerate(reversed(str(num2))):
        _multiple = int(math.pow(10, i))
        multiple = int(_multiple * int(digit))
        value = int(num1) * multiple
        total += value
        values.append(int(value / _multiple))

    values.append(total)
    
    print('\n'.join(map(str, values)))


def run():
    num1 = input().strip()
    num2 = input().strip()
    
    solution(num1, num2)


if __name__ == "__main__":
    run()