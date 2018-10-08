### [1\. Two Sum](https://leetcode.com/problems/two-sum/description/)

Difficulty: **Easy**



Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **_exactly_** one solution, and you may not use the _same_ element twice.

**Example:**

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[**0**] + nums[**1**] = 2 + 7 = 9,
return [**0**, **1**].
```



#### Solution

Language: **Python3**

```python3
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            try:
                j = nums.index(target - nums[i])
                if i == j:
                    raise KeyError("No same key allow")
                return [i, j]
            except:
                pass
```