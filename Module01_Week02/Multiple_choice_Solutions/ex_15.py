def function_helper(x):
    return "T" if x > 0 else "N"


def my_function(data):
    res = [function_helper(x) for x in data]
    return res


if __name__ == '__main__':
    data = [10, 0, -10, -1]
    assert my_function(data) == ["T", "N", "N", "N"]

    data = [2, 3, 5, -1]
    print(my_function(data))
