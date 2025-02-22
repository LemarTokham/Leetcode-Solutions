class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # First split the array into 2
        arr1 = []
        arr2 = []
        for i in range(2*n):
            if i < n:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        
        # Create stack
        stack = []
        for i in range(n):
            num1 = arr1[i]
            num2 = arr2[i]
            stack.append(num1)
            stack.append(num2)
            
        return stack