from collections import Counter
def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    text = get_book_text(book_path)
    print(f"{get_num_words(text)} words found in the document")
    unsorted_chars =get_chars_dict(text)
    chars=dict(sorted(unsorted_chars.items(), key=lambda x: x[1], reverse=True)) 
    for c in chars:
        count =chars[c]
        if c .isalpha() :
            print(f"The '{c}' character was found {count} times")
    print()


    # print(len(words))


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()



main()
