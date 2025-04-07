class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        target, isOdd = divmod(sum(nums), 2)
        if isOdd: return False

        bitmap = reduce(lambda x, y: x|(x << y), nums, 1)
        return bitmap & (1 << target) != 0