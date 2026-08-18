class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for i in range(len(nums)):
            if nums[i] in diff_map:
                return [diff_map[nums[i]], i]
            diff_map[target-nums[i]] = i
        
        