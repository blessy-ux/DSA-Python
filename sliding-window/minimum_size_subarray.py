class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        l = 0
        r = 0
        m = len(nums)
        csum = 0

        while r < n:
            csum += nums[r]

            if csum >= target:
                while csum >= target:
                    ml = r - l + 1
                    m = min(m, ml)
                    csum -= nums[l]
                    l += 1

            r += 1

        if m == n and sum(nums) < target:
            return 0

        return m
