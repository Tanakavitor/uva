def main():
    n = int(input().strip())
    for i in range(n):
        nun = [int(x) for x in input().strip().split()]
        nun.sort()
        print(f"Case{i+1}: {nun[1]}")

if __name__ == "__main__":
    main()