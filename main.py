def readFile(filePath):
    with open(filePath) as f:
        fileContents = f.read()
    return fileContents


def countWords(string):
    count = 0
    for word in string.split():
        count += 1
    return count


def countChars(string):
    chars = {}
    string = string.lower()
    for char in string:
        if char not in chars:
            chars[char] = 1
            continue
        chars[char] += 1
    return chars


def main():
    filePath = "./books/frankenstein.txt"

    fileContents = readFile(filePath)
    words = countWords(fileContents)
    characters = countChars(fileContents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")
    for c in characters:
        if c.isalpha():
            print(f"The '{c}' character was found {characters[c]} times")
    print("--- End report ---")


main()
