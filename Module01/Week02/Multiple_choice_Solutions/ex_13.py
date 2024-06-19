def my_function(y):
    var = 1
    while y > 1:
        var *= y
        y -= 1
    return var


if __name__ == '__main__':
    assert my_function(8) == 40320
    print(my_function(4))
