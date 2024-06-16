def max_kernel(num_list: list, k: int) -> list:
    """
    This function aim to calculate maximum value within a sliding window of size 'k' over a list number

    Parameters:
    -----------
    num_list: list
        A list of number over which the sliding window will slide to calculate the maximum values.

    k: int
        The size of the sliding window. Must be greater than or equal to 1.

    Returns:
    -----------
    list:
        A list containing the maximum values from each sliding window of size 'k' within 'numbers'.

    """

    if k <= 0:
        raise ValueError("k must be greater than or equal to 1")

    max_values = []
    for i in range(0, len(num_list) - k + 1):
        window = num_list[i:i+k]
        max_values.append(max(window))
    return max_values


if __name__ == "__main__":
    assert max_kernel([3 , 4 , 5 , 1 , -44], 3) == [5, 5, 5]
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    print(max_kernel(num_list, k))