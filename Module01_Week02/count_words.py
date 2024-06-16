def word_count(file_path: str) -> dict:
    """
    Count the frequency of each word in a given file text. Words that are counted will be in lowercase form.

    Parameters:
    -----------
    file_path: str
        A path to a file which used to count the words within it.

    Returns:
    dict
        A dictionary with words as keys and their frequency counts as values
    """

    # Reading text from file path
    with open(file_path, "rt", encoding="utf_8") as f:
        lines = f.readlines()

    word_frequency = {}
    # Loop for each line
    for line in lines:
        # Split line into words
        words = line.split()

        # Statistic words
        for word in words:
            word_lowercase = word.lower()
            word_frequency[word_lowercase] = word_frequency.get(
                word_lowercase, 0) + 1

    return word_frequency


if __name__ == "__main__":
    # Exercise 3
    file_path = "./P1_data.txt"
    result = word_count(file_path)
    assert result["who"] == 3
    print(result["man"])
