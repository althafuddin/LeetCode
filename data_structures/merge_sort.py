def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublist created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes O(n log n)
    Takes linear space
    """ 

    if len(list) <=1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right

    Takes overall O(log n)
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs in overall linear time O(n)
    """
    l = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            l.append(left[left_index])
            left_index+=1
        else:
            l.append(right[right_index])
            right_index+=1

    while left_index < len(left):
        l.append(left[left_index])
        left_index+=1
    
    while right_index < len(right):
        l.append(right[right_index])
        right_index+=1

    return l

def verify_sorted(list):

    n = len(list)
    if n <=1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])

a_list = [54,26,1,5,51,32,10,78,0,-24,20]
l = merge_sort(a_list)
print(verify_sorted(a_list))
print(l)
print(verify_sorted(l))