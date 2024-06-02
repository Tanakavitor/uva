count = 0
def tex(string):
    global count
    new = []
    for i in range(0, len(string)):
        if string[i] == "\"":
            count += 1
            if (count % 2) != 0:
                new.append("``")
            else:
                new.append("''")
        else:
            new.append(string[i])
    return ''.join(new)

def main():
    global count
    while True:
        try:
            a = input()
            print(tex(a))
        except EOFError:
            break

if __name__ == "__main__":
    main()