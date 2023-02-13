import sys

def main():

    stackey = list(sys.argv[1])
    
    newW = ""
    noSpace = ""

    for i in stackey:
        if i != ' ':
            noSpace += (i).lower();

    while stackey:
        e = stackey.pop()
        if e != ' ':
            newW += e.lower()

    if newW == noSpace:
        print('Yes\n')
    else:
        print("No\n")

if __name__ == "__main__":
    main()
