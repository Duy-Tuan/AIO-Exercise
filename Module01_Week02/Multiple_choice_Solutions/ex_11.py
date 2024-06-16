def my_function(list_nums = [0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var / len(list_nums)


if __name__ == '__main__':
    assert my_function([4, 6, 8]) == 6
    print(my_function())