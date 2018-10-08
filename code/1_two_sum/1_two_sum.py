class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        revert_indices = dict()
        for index, value in enumerate(nums):
            revert_indices[value] = index
        for i in range(len(nums)):
            try:
                j = revert_indices[target - nums[i]]
                if i == j:
                    raise KeyError("No same key allow")
                return [i, j]
            except:
                pass


solution = Solution()
result = solution.twoSum(nums=[2, 8, 7, 15], target=9)
print(result)
