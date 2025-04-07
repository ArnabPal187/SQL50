from functools import reduce

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        target, isOdd = divmod(sum(nums), 2)
        if isOdd:
            return False
        
        # Create the bitmap to track possible subset sums
        bitmap = 1  # Start with 1, representing the sum of 0
        for num in nums:
            # Update the bitmap by considering the current num
            bitmap |= bitmap << num
        
        # Check if we can form the 'target' sum
        return bitmap & (1 << target) != 0
