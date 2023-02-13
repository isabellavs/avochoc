import sys

def main():

    # using str.replace() since python's version is optimised
    # in C and does not do the whole str concat thing
    # which would happen if I looped through the string 
    # and replaced the offending chars.
    # Not against the rule of not using built in functions to REVERSE the word.

    noSpace = sys.argv[1].replace(' ', '')
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
