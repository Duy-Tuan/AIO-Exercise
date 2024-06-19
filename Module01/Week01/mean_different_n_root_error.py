def md_nre_single_sample(y: float, y_hat: float, n: int, p: int) -> float:
    """
    This function aim to calculate Mean Different of n_th Root Error (MD_nRE) of a sample of prediction-target value

    Parameters:
         y (float): ground truth value
         y_hat (float): prediction value
         n (int): n-th root of loss function
         p (int): degree of the loss function

    Returns:
        float: MD_nRE value of the pair of prediction-target value (y and y_hat).
    """
    loss = pow(pow(y, 1 / n) - pow(y_hat, 1 / n), p)
    return loss


if __name__ == "__main__":
    print(md_nre_single_sample(100, 99.5, 2, 1))
    print(md_nre_single_sample(50, 49.5, 2, 1))
    print(md_nre_single_sample(20, 19.5, 2, 1))
    print(md_nre_single_sample(0.6, 0.1, 2, 1))