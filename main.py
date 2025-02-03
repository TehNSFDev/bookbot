def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_letter(text)
    sorted_list = list_of_dicts(chars_dict)
    print_report(book_path, num_words, sorted_list)


def count_words(text):
    complete_text = text.split()
    return len(complete_text)


def count_letter(text):
    word_count = {}
    lowered_text = text.lower()
    for letter in lowered_text:
        if letter not in word_count:
            word_count[letter] = 1
        else:
            word_count[letter] += 1
    return word_count


def get_book_text(path):
    with open(path) as f:
        return f.read()


def sort_on(dict):
    return dict["num"]


def list_of_dicts(dict):
    dict_list = []
    for item in dict:
        if item.isalpha():
            letter_dict = {}
            letter_dict["letter"] = item
            letter_dict["num"] = dict[item]
            dict_list.append(letter_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


def print_report(book_path, word_count, sorted_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document \n")

    for dict in sorted_list:
        letter = dict["letter"]
        count = dict["num"]
        print(f"The '{letter}' character was found {count} times")
    
    print("--- End report ---")


main()
