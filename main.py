from stats import get_character_count, get_num_words, sort_character_count
import sys


def get_book_text(book_file):
    with open(book_file) as f:
        content = f.read()
    return content


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    contents = []
    if(len(sys.argv) != 2):
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    book_path = sys.argv[1]

    contents = get_book_text(book_path)
    print("----------- Word Count ----------")
    get_num_words(contents)
    characters = get_character_count(contents)
    print("----------- Character Count ----------")
    for cc in sort_character_count(characters):
        name = cc["name"]
        num = cc["num"]
        print(f'{name}: {num}')


main()
