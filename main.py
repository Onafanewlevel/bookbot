import sys
from stats import get_word_count, get_char_count, sort_by_count

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(sys.argv[1])
    word_count = get_word_count(file_contents)
    char_count = get_char_count(file_contents)
    sorted_list = sort_by_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing the book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
