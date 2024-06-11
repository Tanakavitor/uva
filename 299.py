def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return arr, swaps

def main():
    n = int(input().strip())
    for _ in range(n):
        size = int(input().strip())
        arr = list(map(int, input().strip().split()))
        _, swaps = bubble_sort(arr)
        print(f'Optimal train swapping takes {swaps} swaps.')

if __name__ == "__main__":
    main()