class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        revert_indices = dict()
        for i in range(len(nums)):
            try:
                j = revert_indices[target - nums[i]]
                return [j, i]
            except KeyError:
                revert_indices[nums[i]] = i


solution = Solution()
result = solution.twoSum(nums=[2, 8, 7, 15], target=9)
print(result)
