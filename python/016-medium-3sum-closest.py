# time: O(n^2)
# space: O(1)

from math import inf


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        min_diff = inf
        closest_sum = inf

        for i in range(len(nums)-2):
            # i, lo, hi
            lo = i + 1
            hi = len(nums) - 1
            
            while lo < hi:
                current_sum = nums[i] + nums[lo] + nums[hi]
                diff = current_sum - target

                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    closest_sum = current_sum

                if diff < 0:
                    lo += 1
                elif diff > 0:
                    hi -= 1
                else:
                    return target

        return closest_sum


nums = [-1, 2, 1, -4]
target = 1

s = Solution()
assert s.threeSumClosest(nums, 1) == 2
