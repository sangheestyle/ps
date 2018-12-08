# time: O(n^2)
# space: O(1)

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort nums first then we have some order (direction)
        # i, lo, hi
        #   => lo ->  : <- hi
        #   => if nums.sums(i, lo, hi) == 0: i, lo, hi
        # .     nums.sums < 0: we need bigger value -> lo =+ 1
        # .     nums.sums > 0: we need smaller value -> hi -= 1
        # . loop till: lo < hi
        # loop till i .. len(nums) - 2 (i, lo, hi)
        nums.sort()
        combs = []
        
        for i in range(len(nums)-2):
            # skip duplicate
            # how?
            #   -> do first thing
            #   -> if it is not first time(first index)
            #       -> check current to previous index
            if i == 0 or nums[i-1] != nums[i]:
                lo = i + 1
                hi = len(nums) - 1
                
                while (lo < hi):
                    currentSum = nums[i] + nums[lo] + nums[hi]

                    if currentSum < 0:
                        lo += 1
                    elif currentSum > 0:
                        hi -= 1
                    else:
                        # match case
                        combs.append([nums[i], nums[lo], nums[hi]])
                        # what do we need to do with remaining range
                        # -> can we use current lo or hi? -> not -> why? uniqueness
                        lo += 1
                        hi -= 1

                        # seek to another unique one
                        # lo -> compare lo-1, lo
                        while lo < hi and nums[lo-1] == nums[lo]:
                            lo += 1

                        # compare hi, hi+1
                        while lo < hi and nums[hi+1] == nums[hi]:
                            hi -= 1
                        
        return combs


nums = [-1, 0, 1, 2, -1, -4]
expect = [
    [-1, -1, 2],
    [-1, 0, 1],
]
s = Solution()
assert s.threeSum(nums) == expect
