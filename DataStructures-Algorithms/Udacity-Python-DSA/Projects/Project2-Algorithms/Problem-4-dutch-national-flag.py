def sort_012(nums):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       nums(list): List to be sorted
    Returns: Sorted nums
    """
    # Linear search, O(1) in time, O(1) in space
    pos0, pos2 = 0, len(nums)-1
    i = 0
    while i <= pos2 and pos0 < pos2: # Maximum one pass: O(n) in time
        if nums[i] == 0:
            nums[pos0], nums[i] = nums[i], nums[pos0]
            pos0 += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[pos2] = nums[pos2], nums[i]
            pos2 -= 1
        else:
            i += 1
    return nums

# Tests
def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass", end=' ')
    else:
        print("Fail", end=' ')

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
test_function([0])
test_function([1,1])
# Pass Pass Pass Pass Pass Pass 
