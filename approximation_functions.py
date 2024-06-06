import math

def approximate_sin(x: float, n: int) -> float:
    """
    This function aim to calculate approximate value of the sine function of x after n iteration, defined as:
        sin(x) ~ (-1)^i * (x^(2*i + 1)) / (2*i + 1)! for each i in range n

    Parameters:
        x (float): input value in radians
        n (int): Number of iterations desired for approximation

    Returns:
        float: Approximate value of the sine function of x after n iterations.
    """
    sin_x = 0
    for i in range(n):
        sin_x += ((-1) ** i) * (x ** (2 * i + 1)) / (math.factorial(2 * i + 1))
    return sin_x

def approximate_cos(x: float, n: int) -> float:
    """
    This function aim to calculate approximate value of the cosine function of x after n iteration, defined as:
        cos(x) ~ (-1)^i * (x^(2*i)) / (2*i)! for each i in range n

    Parameters:
        x (float): input value in radians
        n (int): Number of iterations desired for approximation

    Returns:
        float: Approximate value of the cosine function of x after n iterations.
    """
    cos_x = 0
    for i in range(n):
        cos_x += ((-1) ** i) * (x ** (2 * i)) / (math.factorial(2 * i))
    return cos_x

def approximate_sinh(x: float, n: int) -> float:
    """
    This function aim to calculate approximate value of the sinh function of x after n iteration, defined as:
        sinh(x) ~ (x^(2*i + 1)) / (2*i + 1)! for each i in range n

    Parameters:
        x (float): input value in radians
        n (int): Number of iterations desired for approximation

    Returns:
        float: Approximate value of the sinh function of x after n iterations.
    """
    sinh_x = 0
    for i in range(n):
        sinh_x += (x ** (2 * i + 1)) / (math.factorial(2 * i + 1))

    return sinh_x

def approximate_cosh(x: float, n: int) -> float:
    """
    This function aim to calculate approximate value of the cosh function of x after n iteration, defined as:
        cosh(x) ~ (x^(2*i)) / (2*i)! for each i in range n

    Parameters:
        x (float): input value in radians
        n (int): Number of iterations desired for approximation

    Returns:
        float: Approximate value of the cosh function of x after n iterations.
    """
    cosh_x = 0
    for i in range(n):
        cosh_x += (x ** (2 * i)) / (math.factorial(2 * i))

    return cosh_x

if __name__ == "__main__":
    print(approximate_sin(x=3.14, n=10))
    print(approximate_cos(x=3.14, n=10))
    print(approximate_sinh(x=3.14, n=10))
    print(approximate_cosh(x=3.14, n=10))
