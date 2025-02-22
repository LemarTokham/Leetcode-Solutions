class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1 # 1 becasue there will always be atleast one unique number, which if repeated first won't be taken into account initially
        l = 0
        r = 1
        for i in range(len(nums)):
            if r < len(nums):
                if nums[l] == nums[r]:
                    nums[r] = 101 # 101 as the max number in the original list is 100, so 101 allows for sorting to be kept the same
                else:
                    k += 1
                    l = r
                r += 1
        nums.sort()
        # Another way to count how many unique numbers there are
        # for i in range(len(nums)): 
        #     if nums[i] != 101:
        #         k += 1
            
        return k