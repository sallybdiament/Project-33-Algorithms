# https://stackoverflow.com/questions/13101468/python-how-to-sort-the-alphabet-in-a-list-without-sorted-functions
def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x < lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))


def check_isInt(nums):
    if nums is None or len(nums) <= 1:
        return False
    for n in nums:
        if type(n) is not int:
            return False
        if n < 0:
            return False
    return True


def find_duplicate(nums):
    if check_isInt(nums) is False:
        return False
    ordered_nums = quicksort(nums)
    repeated = 0
    for i in range(len(ordered_nums) - 1):
        if ordered_nums[i] == ordered_nums[i+1]:
            repeated = ordered_nums[i]
    if repeated != 0:
        return repeated
    else:
        return False
