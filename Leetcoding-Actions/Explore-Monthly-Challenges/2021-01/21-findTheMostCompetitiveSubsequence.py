class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
    
        for idx, num in enumerate(nums):
            min_stack_len = max(0, k - len(nums) + idx)
            while len(stack) > min_stack_len and num < stack[-1]:
                stack.pop()
            stack.append(num)

        return stack[:k]
