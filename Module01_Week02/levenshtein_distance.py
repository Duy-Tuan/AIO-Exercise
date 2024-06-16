def levenshtein_distance(source: str, target: str) -> int:
    """
    Computes the Levenshtein distance between two strings.

    The Levenshtein distance is a measure of the difference between two sequences.
    It is the minimum number of single-character edits (insertions, deletions, or substitutions)
    required to change one string into the other.

    Args:
        source (str): The source string to compare.
        target (str): The target string to compare against the source.

    Returns:
        int: The Levenshtein distance between the source and target strings. This value
        represents the minimum number of single-character edits needed to transform
        the source string into the target string.

    Algorithm:
        1. Prepend a '#' character to both strings to handle edge cases.
        2. Initialize a matrix with the number of rows equal to the length of the source
           and the number of columns equal to the length of the target.
        3. Set the first row and first column of the matrix with incremental values starting
           from 0 up to the length of the corresponding string.
        4. Iterate over each character in both strings, compute the edit values, and update
           the matrix with the minimum edit distance at each step.
        5. The value in the bottom-right cell of the matrix represents the Levenshtein distance
           between the two strings.
    """

    source = "#" + source
    target = "#" + target
    rows = len(source)
    cols = len(target)

    # Initialize empty matrix with size rows x cols
    matrix = [[None] * cols for _ in range(rows)]

    # Initialize first rows and first columns values
    first_rows = list(range(rows))
    first_cols = list(range(cols))

    # Fill the first column and first row of the matrix
    for c in range(cols):
        matrix[0][c] = first_cols[c]
    for r in range(rows):
        matrix[r][0] = first_rows[r]

    # Calculate levenshtein distance between source and target
    for r in range(1, rows):
        for c in range(1, cols):
            insert_value = matrix[r][c - 1] + 1
            delete_value = matrix[r - 1][c] + 1

            if source[r] != target[c]:
                substitution_value = matrix[r - 1][c - 1] + 1
            else:
                substitution_value = matrix[r - 1][c - 1] + 0

            min_value = min([insert_value, delete_value, substitution_value])
            matrix[r][c] = min_value

    return matrix[rows - 1][cols - 1]


if __name__ == "__main__":
    source = "kitten"
    target = "sitting"
    print(levenshtein_distance(source, target))

    # Exercise 4
    assert levenshtein_distance("hi", "hello") == 4.0
    print(levenshtein_distance("hola", "hello"))
