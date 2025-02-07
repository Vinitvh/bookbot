def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        num_of_words(file_contents)
        get_each_char(file_contents)
        report(file_contents)

def num_of_words(text):
    words = text.split()
    words_len = len(words)
    return words_len

def get_each_char(text):
    chars = {}
    for char in text:
        lower = char.lower()
        if lower in chars:
            chars[lower] += 1
        else:
            chars[lower] = 1

    return chars

def report(text):
    words_len = num_of_words((text))
    lst = list(get_each_char(text).items())
    lst.sort(reverse=False)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_len} words found in the document")
    
    for dict in lst:
        if dict[0].isalpha() == True:
            print(f"The '{dict[0]}' character was found {dict[1]} times")
                    
    print("--- End report ---")

main()

