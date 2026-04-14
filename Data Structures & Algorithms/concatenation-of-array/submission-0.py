class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        value = []
        value2 = []
        for num in nums:
            value.append(num)
            value2 = value + value
        return value2   