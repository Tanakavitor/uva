def main():
    n = int(input().strip())
    for _ in range(n):
        s = input().strip()
        stack = []
        balanced = True
        for char in s:
            if char in "[(":
                stack.append(char)
            else:
                if not stack:
                    balanced = False
                    break
                else: 
                    if (char == ")" and stack[-1] == "(") or (char == "]" and stack[-1] == "["):
                        stack.pop()
                    else:
                        balanced = False
                        break
        if balanced and not stack:  
            print("Yes")
        else:  
            print("No")

if __name__ == "__main__":
    main()