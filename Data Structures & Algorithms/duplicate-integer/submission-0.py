#create a new array
#append the values to the new array thats not in there
#compare the length of the new array to the old array
#return true if they are noot equal 
#return false if they are the same length

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        updated_Array = []
        for i in nums:
            if i not in updated_Array:
                updated_Array.append(i)
        if len(updated_Array) == len(nums):
            return False
        return True            
        