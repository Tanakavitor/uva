def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    index = 0
    N = int(data[index])
    index += 1
    results = []
    for _ in range(N):
        dic = {}
        valor = 0
        K = int(data[index])
        index += 1
        for _ in range(K):
            line = data[index]
            char = line[0]
            value = int(line[1:].strip())
            dic[char] = value
            index += 1
        M = int(data[index])
        index += 1
        for _ in range(M):
            line = data[index]
            for char in line:
                if char in dic:
                    valor += dic[char]
            index += 1
        results.append(f'{valor / 100:.2f}$')
    for result in results:
        print(result)
if __name__ == "__main__":
    main()
