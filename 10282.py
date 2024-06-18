import sys

def main():
    dictionary = {}
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        english, foreign = line.split()
        dictionary[foreign] = english

    for line in sys.stdin:
        translate = line.strip()
        print(dictionary.get(translate, 'eh'))

if __name__ == "__main__":
    main()