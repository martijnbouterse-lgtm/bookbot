def get_num_words(book):
    words = book.split()
    return len(words)

def get_num_chars(book):
    char_dict = {}
    for c in book.lower():
        if c not in char_dict:
            char_dict.update({c:1})
        elif c in char_dict:
            char_dict[c] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_char_dict(char_dict):
    sorted_chars = []
    for char in char_dict:
        temp_dict = {
            "char": char,
            "num": char_dict[char]
        }
        sorted_chars.append(temp_dict)
        sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars     