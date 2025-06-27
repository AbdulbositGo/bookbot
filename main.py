import sys

from stats import get_num_chars, get_num_words, get_sorted_dict


def get_book_text(path: str) -> str:
    with open(path) as f:
        file_content = f.read()
    return file_content


def main() -> None:
    if not len(sys.argv) == 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    path = sys.argv[1]
    book = get_book_text(path)
    words = get_num_words(book)
    chars = get_num_chars(book)
    sorted_chars = get_sorted_dict(chars)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {words} total words')
    print('--------- Character Count -------')
    for i in sorted_chars:
        print(f'{i["char"]}: {i["num"]}')


if __name__ == '__main__':
    main()
