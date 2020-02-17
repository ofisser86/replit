def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    return text.split(' ')[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))