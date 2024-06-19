def calculate_precision(tp: int, fp: int) -> float:
    """
    This function aim to compute precision of a classification model

    Parameters:
        tp (int): True Positive
        fp (int): False Positive

    Returns:
        This function returns precision value (a float number between 0 and 1)
    """
    precision = tp / (tp + fp)
    return precision


def calculate_recall(tp: int, fn: int) -> float:
    """
    This function aim to compute recall of a classification model

    Parameters:
        tp (int): True Positive
        fn (int): False Negative

    Returns:
        This function returns recall value (float number between 0 and 1)
    """
    recall = tp / (tp + fn)
    return recall


def calculate_F1_score(precision: float, recall: float) -> float:
    """
    This function aim to compute F1_score of a classification model

    Parameters:
        precision (float): Precision value
        recall (float): Recall value

    Returns:
        This function returns F1_score value (float number between 0 and 1)
    """
    f1_score = 2 * (precision * recall) / (precision + recall)
    return f1_score


def evaluate_result(tp: int, fp: int, fn: int) -> None:
    """
    This function aim to compute precision, recall and F1_score of a classification model

    Parameters:
        tp (int): True Positive, must be larger than 0
        fp (int): False Positive, must be larger than 0
        fn (int): False Negative, must be larger than 0

    Returns:
        None

    Prints:
        This function will print precision, recall and F1_score result.
    """

    # Check input type
    if not isinstance(tp, int):
        print("tp must be int")
        return
    if not isinstance(fp, int):
        print("fp must be int")
        return
    if not isinstance(fn, int):
        print("fn must be int")
        return
    if (tp <= 0) or (fp <= 0) or (fn <= 0):
        print("tp and fp and fn must be greater than zero")
        return

    precision = calculate_precision(tp, fp)
    recall = calculate_recall(tp, fn)
    f1_score = calculate_F1_score(precision, recall)

    print(f"Precision is {precision}")
    print(f"Recall is {recall}")
    print(f"F1-score is {f1_score}")


if __name__ == "__main__":
    # evaluate_result(tp=2, fp=3, fn=4)
    # evaluate_result(tp=2, fp="a", fn=4)
    # evaluate_result(tp=2, fp=3, fn="a")
    # evaluate_result(tp=2, fp=3, fn=0)
    evaluate_result(tp=2.1, fp=3, fn=0)
