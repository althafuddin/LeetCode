def linear_search(list, target):
    """
    returns the postion of the index postion if target if found, else returns none - O(n)
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found at index")

numbers = [1,2,3,4,5,6,7,8,9,10]

results=linear_search(numbers, 6)
verify(results)