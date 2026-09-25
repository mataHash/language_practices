def merge_sort(list):
    """
    Sorts a list in ascending order and returns new sorted list
    divide:
    find the midpoint of the list and divide into sublist
    conquer: Recursively sort the sublist created in previous step
    combine: Merge the sorted sublist created in previous step
    """
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Return two sublist - left and right
    """
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    return left, right


def merge(left, right):
    """
    merges two lists, sorting tgem in the process
    Return a new merged list
    """
    list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            list.append(left[i])
            i += 1
        else:
            list.append(right[j])
            j += 1
    while i < len(left):
        list.append(left[i])
        i += 1
    while j < len(right):
        list.append(right[j])
        j += 1
    return list


def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    return list[0] < list[1] and verify_sorted(list[1:])


alist = [32, 73, 45, 12, 234, 234567, 1123, 20395872034,
         234, 985, 23, 96, 12341, 495, 234, 123, 10, 8]
print(verify_sorted(alist))
