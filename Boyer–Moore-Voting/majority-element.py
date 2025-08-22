class Solution:
    def majorityElement(self, nums) -> int:
        vote = 0
        candidate = None

        for num in nums:
            if vote == 0:
                candidate = num
            vote += 1 if num == candidate else -1

        if nums.vote(candidate) > len(nums) // 2:
            return candidate
        return -1
