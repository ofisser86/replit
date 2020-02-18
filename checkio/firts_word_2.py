def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    x = text.replace('.', ' ').replace(',', ' ').split()
    
    return x[0]


if __name__ == '__main__':
    print("Example:")
    #print(first_word("Hello world"))
    print(first_word("..,. Hello.W,orld"))