from stats import get_num_words, get_num_characters

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    # print(book_text)
    words_number = get_num_words(book_text)
    print(f"words in book {words_number}")
    char_number = get_num_characters(book_text)
    print(f"number of characters in text: {char_number}")

main()