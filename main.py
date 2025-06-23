from stats import get_num_words, get_num_characters, make_dict_list, sort_characters_dict_list

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    char_number = get_num_characters(book_text)
    # print(f"number of characters in text: {char_number}")
    dict_list = make_dict_list(char_number)
    sorted_dict_list = sort_characters_dict_list(dict_list)

    for entry in sorted_dict_list:
        print(entry)

main()
