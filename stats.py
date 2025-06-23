def get_num_words(text):
    number_of_words = text.split()
    return len(number_of_words)

def get_num_characters(text):
    lower_case_text = text.lower()
    words = lower_case_text.split()
    number_of_chars = {}
    for word in words:
        for char in word:
            if char in number_of_chars:
                number_of_chars[char] += 1
            else:
                number_of_chars[char] = 1
    return number_of_chars

def make_dict_list(char_dict):
    char_list = []
    for char in char_dict:
        char_element = {"name": char, "num": char_dict[char]}
        char_list.append(char_element)
    return char_list

def sort_on(char_dict):
    return char_dict

def sort_characters_dict(char_dict):
    return char_dict
