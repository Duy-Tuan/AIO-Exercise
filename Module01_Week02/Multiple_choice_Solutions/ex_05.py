def check_the_number(n):
    """
    Check if an input number is in the list of numbers from 1 to 4.

    Parameters:
    N : int
        The number to check.

    Returns:
    str
        "True" if the number is in the list [1, 2, 3, 4], otherwise "False".
    """
    list_of_numbers = []
    results = ""
    for i in range(1, 5):
        list_of_numbers.append(i)

    if n in list_of_numbers:
        results = "True"
    if n not in list_of_numbers:
        results = "False"

    return results


if __name__ == "__main__":
    N = 7
    assert check_the_number(N) == "False"

    N = 2
    results = check_the_number(N)
    print(results)
