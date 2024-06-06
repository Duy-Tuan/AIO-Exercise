import math


def sigmoid(x: float) -> float:
    """
    This function aim to compute the sigmoid of input x is defined as 1 / (1 + exp(-x))

    Parameters:
        x (float): The input value

    Returns:
        float: Sigmoid value of the input.
    """
    return 1 / (1 + math.exp(-x))


def relu(x: float) -> float:
    """
    This function aim to compute the ReLU (Rectified Linear Unit) of input x, defined as:
        - If x > 0, return x
        - If x <= 0, return 0

    Parameters:
        x (float): The input value

    Returns:
        float: ReLU value of the input.
    """
    if x > 0:
        return x
    else:
        return 0


def elu(x: float) -> float:
    """
    This function aim to compute the ELU (Exponential Linear Unit) of input x, defined as:
        - If x > 0, return x
        - If x <= 0, return alpha * (exp(x) - 1), alpha = 0.01

    Parameters:
        x (float): The input value

    Returns:
        float: ELU value of the input.
    """
    alpha = 0.01
    if x > 0:
        return x
    else:
        return alpha * (math.exp(x) - 1)


def is_number(n):
    try:
        # Type-casting the string to ‘float‘.
        float(n)
    # If string is not a valid ‘float ‘,it’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True

def calculate_activation() -> None:
    """
    This function prompts the user to input the value of x and desired activation function (sigmoid, relu, elu),
    computes the selected activation function of the input x. Then print the result to user.

    Parameters:
        None

    Returns:
        None

    Prints:
        Print the specified activation result of the input value from the user.
    """
    x = input("Input x = ")

    if not is_number(x):
        print("x must be a number")
        return

    x = float(x)
    activation = input("Input activation function (sigmoid|relu|elu): ")
    if activation not in ("sigmoid", "relu", "elu"):
        print(f"{activation} is not supported")
        return

    if activation == "sigmoid":
        result = sigmoid(x)
        print(f"Sigmoid: f({x}) = {result}")
    elif activation == "relu":
        result = relu(x)
        print(f"ReLU: f({x}) = {result}")
    else:
        result = elu(x)
        print(f"ELU: f({x}) = {result}")


if __name__ == "__main__":
    calculate_activation()