class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for key in nums:

            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1

        for key, value in dic.items():
            if value > len(nums)//2:
                return key
        