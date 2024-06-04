def main():
    t = int(input().strip())
    for _ in range(t):
        input() 
        order = list(map(int, input().strip().split()))
        numbers = input().strip().split()
        n = len(order)
        new = ['']*n
        for i in range(n):
            new[order[i]-1] = numbers[i]
        for num in new:
            print(num)
        if _ < t-1:
            print() 
if __name__ == "__main__":
    main()