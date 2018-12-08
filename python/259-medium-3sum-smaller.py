class Solution:
    def threeSumSmallerTake1(self, nums, target):
        """
        time: O(n^2)
        space: O(1)
        """
        nums.sort()
        numComb = 0

        for i in range(len(nums)-2):
            lo = i + 1
            hi = len(nums) - 1

            while (lo < hi):
                if nums[i] + nums[lo] + nums[hi] < target:
                    numComb += hi - lo
                    lo += 1
                else:
                    hi -= 1

        return numComb


nums = [-2, 0, 1, 3]
target = 2

s = Solution()
assert s.threeSumSmallerTake1(nums, target) == target
