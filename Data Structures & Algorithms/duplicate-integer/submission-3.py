class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup_check = set()
        for i in range(len(nums)):
            if nums[i] in lookup_check:
                return True
            lookup_check.add(nums[i])
        return False

        