def my_function(n):
    return max(n)


if __name__ == '__main__':
    my_list = [1001, 9, 100, 0]
    assert my_function((my_list)) == 1001

    my_list = [1, 9, 9, 0]
    print(my_function(my_list))
