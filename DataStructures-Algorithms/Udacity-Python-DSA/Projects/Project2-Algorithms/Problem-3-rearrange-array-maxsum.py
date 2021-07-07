def rearrange_digits(nums):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       nums(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(nums) == 0: return [0, 0]
    if len(nums) == 1: return [nums[0], 0]
    nums.sort(reverse=True) # uses sample sort, O(n log n) in time, O(1) in space
    num1, num2 = [], []
    for i, num in enumerate(nums): # O(n) in time
        if i%2 == 0:
            num1.append(str(num)) # O(n/2) in space
        else:
            num2.append(str(num)) # O(n/2) in space
    return [int(''.join(num1)), int(''.join(num2))]

    
# def list2int(nums): # O(n) in time, O(1) in space
#     sum_ = 0
#     for k,num in enumerate(nums[::-1]):
#         sum_ += num * 10**k
#     return sum_

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass", end=' ')
    else:
        print("Fail", end=' ')

# Tests
test_function([[1, 2, 3, 4, 5], [531, 42]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[],[0,0]])
test_function([[1],[1,0]])
test_function([[1,2],[2,1]])
test_function([[4,0,0],[40,0]])
# Pass Pass Pass Pass Pass Pass 
