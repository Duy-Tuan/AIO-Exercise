import torch
import torch.nn as nn
import math


class Softmax(nn.Module):
    """
    Implements the softmax function in PyTorch.

    This class is a neural network module that computes the softmax of its input.
    The softmax function converts input values into a probability distribution.

    Methods
    -------
    forward(x):
        Performs the forward pass of the softmax function.
    """

    def __init__(self):
        super().__init__()

    def forward(self, x):
        """
        Forward pass for the Softmax function.

        Parameters
        ----------
        x : torch.Tensor
            The input tensor for which to compute the softmax.

        Returns
        -------
        torch.Tensor
            A tensor where each value is the result of the softmax function applied to the input.
        """
        exp_x = torch.exp(x)
        return exp_x / torch.sum(exp_x)


class SoftmaxStable(nn.Module):
    """
    Implements a stable version of the softmax function in PyTorch.

    This class is a neural network module that computes the softmax of its input
    in a way that avoids numerical instability for large input values by subtracting
    the maximum value from the input tensor before applying the exponential function.

    Methods
    -------
    forward(x):
        Performs the forward pass of the stable softmax function.
    """

    def __init__(self):
        super().__init__()

    def forward(self, x):
        """
        Forward pass for the stable Softmax function.

        Parameters
        ----------
        x : torch.Tensor
            The input tensor for which to compute the softmax.

        Returns
        -------
        torch.Tensor
            A tensor where each value is the result of the softmax function applied
            to the input, adjusted for numerical stability.
        """
        x_max = torch.max(x, dim=0, keepdims=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp / partition


if __name__ == "__main__":
    # Exercise 1
    print("Exrcise 1")
    print("-"*20)
    data = torch.Tensor([1, 2, 3])
    softmax_function = nn.Softmax(dim=0)
    output = softmax_function(data)
    assert math.isclose(round(output[0].item(), 2), 0.09)
    print(output)

    # Exercise 2
    print("\nExrcise 2")
    print("-"*20)
    data = torch.Tensor([5, 2, 4])
    my_softmax = Softmax()
    output = my_softmax(data)
    assert math.isclose(round(output[-1].item(), 2), 0.26)
    print(output)

    # Exercise 3
    print("\nExrcise 3")
    print("-"*20)
    data = torch.Tensor([1, 2, 300000000])
    my_softmax = Softmax()
    output = my_softmax(data)
    assert math.isclose(round(output[0].item(), 2), 0.0)
    print(output)

    # Exercise 4
    print("\nExrcise 4")
    print("-"*20)
    data = torch.Tensor([1, 2, 3])
    softmax_stable = SoftmaxStable()
    output = softmax_stable(data)
    assert math.isclose(round(output[-1].item(), 2), 0.67)
    print(output)
