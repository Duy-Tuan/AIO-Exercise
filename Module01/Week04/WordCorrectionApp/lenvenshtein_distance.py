def cal_levenshtein_distance(source: str, target: str) -> int:
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
