import sys

from stats import get_num_words, get_num_characters, make_dict_list, sort_characters_dict_list

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def print_report(file_path, word_count, dict_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in dict_list:
        print(f"{entry["name"]}: {entry["num"]}")
    print("============= END ===============")

def main():
    try:
        book_text = get_book_text(sys.argv[1])
    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    word_number = get_num_words(book_text)
    char_number = get_num_characters(book_text)
    dict_list = make_dict_list(char_number)
    sorted_dict_list = sort_characters_dict_list(dict_list)
    print_report(sys.argv[1], word_number, sorted_dict_list)

main()
