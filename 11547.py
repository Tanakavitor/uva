import math

def main():
    n = int(input().strip())
    for _ in range(n):
        t = float(input().strip())
        result = abs((((t * 567 / 9) + 7492) * 235 / 47) - 498)
        print(int(result) % 100 // 10)

if __name__ == "__main__":
    main()