vocabs = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

def solution(word):
    for vocab in vocabs:
        word = word.replace(vocab, "*")
    
    return len(word)


def read_input():
    case = input().strip()

    return case


def run():
    case = read_input()
    print(solution(case))

    # cases = [
    #     "ljes=njak",
    #     "ddz=z=",
    #     "nljj",
    #     "c=c=",
    #     "dz=ak",
    # ]

    # for case in cases:
    #     res = solution(case)
    #     print(res)


if __name__ == "__main__":
    run()