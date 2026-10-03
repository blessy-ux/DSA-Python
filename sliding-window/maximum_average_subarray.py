class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        csum = sum(nums[:k])
        m = csum

        for i in range(k, len(nums)):
            csum = csum - nums[i-k] + nums[i]
            m = max(m, csum)

        return m / k
