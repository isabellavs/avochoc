import sys

def main():
    stackey = list(sys.argv[1])
    otherStackey = []

    print(stackey)
    otherStackey.append(stackey.pop())
    print(stackey, otherStackey)

if __name__ == "__main__":
    main()
