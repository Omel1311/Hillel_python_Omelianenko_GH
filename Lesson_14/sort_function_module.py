"""
Sorting functions module

This module contains the three simplest sorting functions:
    - Bubble sort function
    - Quick sort function
    - Selection sort function

"""
__all__ = ['bubble_sort', 'quick_sort', 'selection_sort']  # ignore def ignore(n, *f):


def bubble_sort(l1: list) -> list:
    """
    Bubble sort function.

    Bubble sort is a sorting algorithm that compares two adjacent elements
    and swaps them until they are in the intended order.

    Keyword arguments:
    :param l1: [n1, n2, n3....]
    :return: l1

    """

    for i in range(0, len(l1) - 1):
        for j in range(len(l1) - 1):
            if l1[j] > l1[j + 1]:
                temp = l1[j]
                l1[j] = l1[j + 1]
                l1[j + 1] = temp
    return l1


def partition(nums: list, low, high):
    """
    Quick sort function
    (additional function to "quick_sort function").

    Divide the collection in two (roughly) equal parts by taking a
    pseudo-random element and using it as a pivot.


    Keyword arguments:
    :param nums: list
    :param low: low - 1 (no need to input data)
    :param high: high + 1 (no need to input data)
    :return: j

    """
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1

        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    """
    Quick sort function (main function).

    Elements smaller than the pivot get moved to the left of the pivot,
    and elements larger than the pivot to the right of it.
    This process is repeated for the collection to the left of the pivot,
     as well as for the array of elements to the right of the pivot until
     the whole array is sorted.

    Keyword arguments:
    :param nums: list [n1, n2, n3....]

    """
    def _quick_sort(items, law, high):
        if law < high:
            split_index = partition(items, law, high)
            _quick_sort(items, law, split_index)
            _quick_sort(items, split_index+1, high)

    _quick_sort(nums, 0, len(nums)-1)


def selection_sort(list_1: list) -> list:  # intentionally "list" (PEP 8)
    """
    Selection sort function.

    Selection sort breaks the input list in two parts, the sorted part which initially is empty,
    and the unsorted part, which initially contains
    the list of all elements.
    The algorithm then selects the minimum value of all the unsorted file and swaps it with
    the first unsorted value, and then increases the sorted part by one.

    Keyword arguments:
    :list_1: list[n1, n2, n3....]
    :i: indicates how many items were sorted

    """
    for i in range(len(list_1) - 1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(list_1) - 1):
            # Update the min_index if the element at j is lower than it
            if list_1[j] < list_1[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        list_1[i], list_1[min_index] = list_1[min_index], list_1[i]
    return list_1


def ignore(n, *f):
    rez = False
    for i in f:
        for j in f:
            if i + j == n:
                rez = True
    print(f'Тест 1: {rez}')
    return rez


if __name__ == "__main__":

    list1 = [6666, 5, 5, 1, -3, 7777777]
    print()
    print("The unsorted list in 'Bubble sort function' is: ", list1)
    # Calling the bubble sort function
    print("The sorted list in 'Bubble sort function' is: ", bubble_sort(list1))
    print()

    list_1 = [66, 5, 89, 1, -3, 55577]
    print("The unsorted list in 'Selection_sort function' is: ", list_1)
    # Calling the bubble sort function
    selection_sort(list_1)
    print("The sorted list in 'Selection_sort function' is: ", list_1)
    print()

    test_lst = [33, 55, 6666, 7, 6, 1, 9]
    print("The unsorted list in 'Quick sort function' is: ", test_lst)
    # Calling the bubble sort function
    quick_sort(test_lst)
    print("The sorted list in 'Quick sort function' is: ", test_lst)
    print()


