cache = {1: 1}

def collatz_length(n):
    if n not in cache:
        cache[n] = collatz_length(n // 2) + 1 if n % 2 == 0 else collatz_length(3 * n + 1) + 1
    return cache[n]

def max_collatz_length(a, b):
    m = 0
    for num in range(a, b + 1):
        m = max(m, collatz_length(num))
    return m

def main():
    while True:
        try:
            a, b = map(int, input().split())
            print(f"{a} {b} {max_collatz_length(min(a, b), max(a, b))}")
        except EOFError:
            break

if __name__ == "__main__":
    main()