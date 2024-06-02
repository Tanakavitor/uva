def scramble(string):
    new = []
    string2 = string.split(" ")
    for i in range(0, len(string2)):
        new.append(string2[i][::-1])
    return ' '.join(new)

def main():
    while True:
        try:
            a = input()
            print(scramble(a))
        except EOFError:
            break

if __name__ == "__main__":
    main()