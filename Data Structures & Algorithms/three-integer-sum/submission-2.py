class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = - nums[i]

            k = len(nums)-1
            j = i+1
            while j < k :
                if nums[k] + nums[j] > target:
                    k -= 1
                elif nums[k] + nums[j] < target :
                    j += 1
                else :
                    result.append([nums[i],nums[j],nums[k]])
                    k -= 1
                    j += 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1


        return result
    
       