from sort_function_module import*

if __name__ == "__main__":

    list1 = [6666, 5, 5, 1, -3, 7777777]
    print()
    print("The unsorted list in 'Bubble sort function' is: ", list1)
    # Calling the bubble sort function
    bubble_sort(list1)
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


print(dir())
