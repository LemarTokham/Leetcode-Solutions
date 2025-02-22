class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Count and how many elements aren't equal to val and those that are equal to them remove them
        k_elements = 0
        for i in range(len(nums)):
            if val != nums[i]:
                k_elements += 1
            else:
                nums[i] = -1
        # All the elements that aren't val will be at the front
        nums.sort(reverse = True)
        return k_elements
       