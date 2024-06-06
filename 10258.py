def main():
    n = int(input().strip())
    input()  
    for _ in range(n):
        dic = {}
        while True:
            try:
                line = input().strip()
                if line == '':
                    break  
                contestant, problem, time, result = line.split()
                contestant = int(contestant)
                problem = int(problem) - 1  
                time = int(time)
                if contestant not in dic:
                    dic[contestant] = {"problems": [0]*9, "penalty": [0]*9}
                if result == 'C':
                    if dic[contestant]["problems"][problem] == 0:
                        dic[contestant]["problems"][problem] = time + dic[contestant]["penalty"][problem] * 20
                elif result == 'I':
                    if dic[contestant]["problems"][problem] == 0:
                        dic[contestant]["penalty"][problem] += 1
            except EOFError:
                break

        for contestant, data in dic.items():
            correct = sum(1 for time in data["problems"] if time > 0)
            time_penalty = sum(time for time in data["problems"] if time > 0)
            dic[contestant] = {"correct": correct, "time_penalty": time_penalty}

        for contestant, data in sorted(dic.items(), key=lambda x: (-x[1]["correct"], x[1]["time_penalty"], x[0])):
            print(f"{contestant} {data['correct']} {data['time_penalty']}")

        if _ < n - 1:
            print()  

if __name__ == "__main__":
    main()