def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    if symbol not in text or text.count(symbol) == 1:
        return None
        
    return text.find(symbol, text.find(symbol)+1, len(text))


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))