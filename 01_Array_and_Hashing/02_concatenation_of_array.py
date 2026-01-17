from typing import List


class Solution1:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.append(i)
        for i in nums:
            ans.append(i)
        
        return ans
        
class Solution2:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans

class Solution3:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2*n)
        for i, num in enumerate(nums):
            ans[i] = ans[i + n] = num
        return ans
    
