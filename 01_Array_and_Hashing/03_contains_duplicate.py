from typing import List


class Solution1:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            if num in dict: 
                return True
            else: dict[num] = 1
        
        return False
    
class Solution2:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    # here i and j are indexes (brute force)

class Solution3:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

class Solution4:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

class Solution5:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)