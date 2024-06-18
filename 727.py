import sys

def main():
    rank = {'+': 1, '-': 1, '*': 2, '/': 2}
    input = sys.stdin.read
    data = input().splitlines()
    
    test_cases = int(data[0])
    index = 1
    
    while index < len(data) and data[index] == "":
        index += 1  
    
    for _ in range(test_cases):
        stack = []
        postfix = []
        
        while index < len(data):
            x = data[index].strip()
            index += 1
            if x == "":
                break
            if x.isalnum():
                postfix.append(x)
            elif x == "(":
                stack.append(x)
            elif x == ")":
                while stack and stack[-1] != "(":
                    postfix.append(stack.pop())
                stack.pop() 
            else:
                while stack and stack[-1] != "(" and rank[x] <= rank[stack[-1]]:
                    postfix.append(stack.pop())
                stack.append(x)
        
        while stack:
            postfix.append(stack.pop())
        
        print(''.join(postfix))
        if _ != test_cases - 1:
            print()
        
        while index < len(data) and data[index] == "":
            index += 1  

if __name__ == "__main__":
    main()
