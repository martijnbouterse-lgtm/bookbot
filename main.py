import sys

from stats import get_num_words,get_num_chars,sort_char_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
#    bookpath = "books/frankenstein.txt"
    bookpath = sys.argv[1]
    book = get_book_text(bookpath)
    num_words = get_num_words(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_chars = sort_char_dict(get_num_chars(book))
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
         return f.read()

main()
