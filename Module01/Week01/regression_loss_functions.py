import random
import math


def generate_sample():
    """
    This function aim to generate two random float number between 0 and 10, representing a prediction and a target value.

    Parameters:
        None

    Returns:
        tuple: A tuple containing two float values. The first value is the prediction and the second value is the target.
    """
    pred = random.uniform(0, 10)
    target = random.uniform(0, 10)
    return pred, target


def mae(number_of_samples: int) -> None:
    """
    This function aim to calculate the Mean Absolute Error (MAE) for a specified number of sample. First,
    it will generate a specified number of random prediction-target pairs,then calculate the MAE for each pair and
    print the loss for each sample. Final, it computes and prints the final MAE over all samples.

    Parameters:
        number_of_samples (int): The number of prediction-target samples to generate and evaluate

    Returns:
        None

    Prints:
        Prints the loss for each pair of random prediction-target pairs, finally prints the MAE of over all samples.
    """
    total = 0

    for i in range(number_of_samples):
        pred, target = generate_sample()

        loss = abs(pred - target)
        print(f"loss name: MAE, sample: {i}, pred: {pred}, target: {target}, loss: {loss}")
        total += loss

    final_mae = total / number_of_samples
    print(f"Final MAE: {final_mae}")


def mse(number_of_samples: int) -> None:
    """
    This function aim to calculate the Mean Square Error (MSE) for a specified number of sample. First,
    it will generate a specified number of random prediction-target pairs,then calculate the MAE for each pair and
    print the loss for each sample. Final, it computes and prints the final MAE over all samples.

    Parameters:
        number_of_samples (int): The number of prediction-target samples to generate and evaluate

    Returns:
        None

    Prints:
        Prints the loss for each pair of random prediction-target pairs, finally prints the MAE of over all samples.
    """

    total = 0

    for i in range(number_of_samples):
        pred, target = generate_sample()

        loss = math.pow((pred - target), 2)
        print(f"loss name: MSE, sample: {i}, pred: {pred}, target: {target}, loss: {loss}")

        total += loss

    final_mse = total / number_of_samples
    print(f"Final MSE: {final_mse}")


def rmse(number_of_samples: int) -> None:
    """
    This function aim to calculate the Root Mean Absolute Error (RMSE) for a specified number of sample. First,
    it will generate a specified number of random prediction-target pairs,then calculate the MAE for each pair and
    print the loss for each sample. Final, it computes and prints the final MAE over all samples.

    Parameters:
        number_of_samples (int): The number of prediction-target samples to generate and evaluate

    Returns:
        None

    Prints:
        Prints the loss for each pair of random prediction-target pairs, finally prints the MAE of over all samples.
    """
    total = 0

    for i in range(number_of_samples):
        pred, target = generate_sample()

        loss = math.pow((pred - target), 2)
        print(f"loss name: RMSE, sample: {i}, pred: {pred}, target: {target}, loss: {loss}")

        total += loss

    final_mse = math.sqrt(total / number_of_samples)

    print(f"Final RMSE: {final_mse}")


def calculate_regression_loss() -> None:
    """
    This function prompts the user to input the number of sample and desired loss name (MAE, MSE, RMSE). Then it
    will, calculate the specified loss function of the random prediction-target pair and print the result.

    Parameters:
        None

    Returns:
        None

    Prints: Prints the loss for each pair of random prediction-target pairs, finally prints the specified loss of
    over all samples.
    """
    number_of_samples = input("Input number of samples (integer number) which are generated: ")

    if not number_of_samples.isnumeric():
        print("Number of samples must be integer number")
        return

    # Type-casting numbers of samples to integer
    number_of_samples = int(number_of_samples)

    loss_name = input("Input loss name: ")
    loss_name = loss_name.upper()
    if loss_name not in ("MAE", "MSE", "RMSE"):
        print(f"Loss name {loss_name} is not supported")
        return

    if loss_name == "MAE":
        mae(number_of_samples)
    elif loss_name == "MSE":
        mse(number_of_samples)
    else:
        rmse(number_of_samples)


if __name__ == "__main__":
    calculate_regression_loss()
