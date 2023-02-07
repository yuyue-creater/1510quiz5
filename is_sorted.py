def is_sorted(integer_list):
    """
    Verify if the list is sorted

    :param integer_list: a list of integers
    :precondition: the list must only contain integers (can be both positive or negative)
    :post-condition: determines if the numbers in the list are sorted in increasing order
    :return: Returns true if the integers in the list are in increasing order, false otherwise

    >>> is_sorted([1, 2, 3])
    True
    >>> is_sorted([3, 1, 2])
    False
    """
    if len(integer_list) == 0:
        return False

    for i in range(1, len(integer_list)):
        if integer_list[i-1] > integer_list[i]:
            return False
    return True
