def count_chars(string: str) -> dict:
    """
    Count the frequency of each character in a given string

    Parameters:
    -----------
    string: str
        A string used to count the characters within it.

    Returns:
    -----------
    dict
        A dictionary with characters as keys and their frequency counts as values

    """
    char_frequency = {}
    for char in string:
        frequency = char_frequency.get(char, 0)
        char_frequency[char] = frequency + 1

    return char_frequency


if __name__ == "__main__":
    assert count_chars("Baby") == {"B": 1, "a": 1, "b": 1, "y": 1}
    print(count_chars("smiles"))
