# https://stackoverflow.com/questions/13101468/python-how-to-sort-the-alphabet-in-a-list-without-sorted-functions
def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x < lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))


def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False
    lower_first = first_string.lower()
    lower_second = second_string.lower()
    ord_first = ''.join(quicksort(lower_first))
    ord_second = ''.join(quicksort(lower_second))

    if ord_first == ord_second:
        return (ord_first, ord_second, True)
    else:
        return (ord_first, ord_second, False)
