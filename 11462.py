def main():
    while True:
        n = int(input().strip())
        if n == 0:
            break
        lista = list(map(int, input().strip().split()))
        max_val = max(lista)
        count = [0] * (max_val + 1)
        for num in lista:
            count[num] += 1
        list2 = []
        for i, num in enumerate(count):
            list2.extend([i] * num)
        print(' '.join(map(str, list2)))

if __name__ == "__main__":
    main()