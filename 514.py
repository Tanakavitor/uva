def main():
    while True:
        n = int(input().strip())
        if n == 0:
            break
        while True:
            sequence = list(map(int, input().strip().split()))
            if sequence[0] == 0:
                break
            stack = []
            j = 0
            for i in range(1, n + 1):
                stack.append(i)
                while stack and stack[-1] == sequence[j]:
                    stack.pop()
                    j += 1
            if stack:
                print("No")
            else:
                print("Yes")
        print()

if __name__ == "__main__":
    main()