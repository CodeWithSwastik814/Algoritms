class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        out = []
        for i in range(n):
            for j in range(i + 1, n):
                x = nums[i] + nums[j]
                if target == x:
                    out.append(i)
                    out.append(j)
                    return out
            