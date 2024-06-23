from collections import deque

def main():
    n_test = int(input().strip())
    for _ in range(n_test):
        ferry_length, cars_waiting = map(int, input().strip().split())  
        ferry_length *= 100  

        queues = {'left': deque(), 'right': deque()}

        for _ in range(cars_waiting):
            car_length, bank = input().strip().split()
            queues[bank].append(int(car_length))

        ferryPos = 'left'
        crossings = 0
        while queues['left'] or queues['right']:
            current_load = 0
            while queues[ferryPos] and current_load + queues[ferryPos][0] <= ferry_length:
                current_load += queues[ferryPos].popleft()
            
            ferryPos = 'right' if ferryPos == 'left' else 'left'  
            crossings += 1

        print(crossings)

if __name__ == "__main__":
    main()



        



