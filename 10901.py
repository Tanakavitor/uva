from collections import deque

def simulateFerry(n, t, m, carDetails):
    queues = {'left': deque(), 'right': deque()}
    unloadTimes = [0] * m
    currentTime = 0
    ferryPos = 'left'

    for i, (arrivalTime, bank) in enumerate(carDetails):
        queues[bank].append((arrivalTime, i))

    while queues['left'] or queues['right']:
        nextTime = float('inf')
        for bank in ['left', 'right']:
            if queues[bank] and queues[bank][0][0] <= currentTime:
                nextTime = currentTime
                break
            elif queues[bank]:
                nextTime = min(nextTime, queues[bank][0][0])

        currentTime = max(currentTime, nextTime)
        loadCount = 0

        while queues[ferryPos] and queues[ferryPos][0][0] <= currentTime and loadCount < n:
            _, carIndex = queues[ferryPos].popleft()
            unloadTimes[carIndex] = currentTime + t
            loadCount += 1

        currentTime += t
        ferryPos = 'right' if ferryPos == 'left' else 'left'

    return unloadTimes

def main():
    test_cases = int(input().strip())
    for case_number in range(test_cases):
        n, t, m = map(int, input().strip().split())
        carDetails = [tuple(input().strip().split()) for _ in range(m)]
        carDetails = [(int(arrivalTime), bank) for arrivalTime, bank in carDetails]
        unloadTimes = simulateFerry(n, t, m, carDetails)
        for time in unloadTimes:
            print(time)
        if case_number < test_cases - 1:  
            print() 

if __name__ == "__main__":
    main()