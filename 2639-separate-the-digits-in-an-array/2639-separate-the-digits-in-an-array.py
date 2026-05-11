class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            temp  = []
            while num:
                temp.append(num%10)
                num = num // 10
            answer.extend(temp[::-1])
        return answer