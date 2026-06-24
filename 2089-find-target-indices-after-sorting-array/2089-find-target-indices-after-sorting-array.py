class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        local=[]
        for i in range(len(nums)):
            if nums[i] == target:
                local.append(i)
        return local
        
        