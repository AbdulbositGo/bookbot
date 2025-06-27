from typing import List


def get_num_words(text: str) -> None:
    return len(text.split(' '))


def get_num_chars(text: str) -> None:
    result = {}
    chars = set()
    for char in text:
        char = char.lower()
        if char in chars:
            result[char] += 1
        else:
            result[char] = 1
            chars.add(char)
    return result


def get_sorted_dict(chars: dict) -> List[dict]:
    result = []

    for k, v in chars.items():
        result.append({'char': k, 'num': v})
    result.sort(reverse=True, key=lambda x: x['num'])

    return result
