def my_function(x):
    return x[::-1]


if __name__ == '__main__':
    x = "I can do it"
    assert my_function(x) == "ti od nac I"

    x = "apricot"
    print(my_function(x))
