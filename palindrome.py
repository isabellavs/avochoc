import sys

def main():

    inStr = sys.argv[1]

    # using str.replace() since python's version is optimised, in C and does not do the whole str concat thing
    # that would happen if I loop through the string and replaced the offending chars.
    noSpace = inStr.replace(' ', '')
    stackey = list(noSpace)
    newW = ""

    while stackey:
        newW += stackey.pop()

    if newW.lower() == noSpace.lower():
        print('Yes\n')
    else:
        print("No\n")

if __name__ == "__main__":
    main()
