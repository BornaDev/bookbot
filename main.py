def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    alpha_dict = only_letters(chars_dict)
    dict_to_list = dict_list(alpha_dict)
    sorted_list = sorting_dict(dict_to_list)
    
    print(f"""--- Begin report of {book_path} --- 
    {num_words} words found in this book
    """)
    for i in sorted_list:
        print(f"""The '{i['char']}' character was found in {i['count']} times""")
    print("--- End of Report ---")

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

def only_letters(chars):
    new_dict = {}
    for c, count in chars.items():
        if c.isalpha():
            new_dict[c] = count
    return new_dict

def dict_list(alpha_dict):
    char_list = []
    for char, count in alpha_dict.items():
        char_list.append({"char": char, "count": count})
    return char_list

def get_count(dict_to_list):
    return dict_to_list["count"]

def sorting_dict(dict_to_list):
    sorted_list = sorted(dict_to_list, key=get_count, reverse=True)
    return sorted_list
main()
