from collections import deque
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        queue = deque([])
        for i in range(1,10):
            queue.append(i)
        
        result = []

        while queue:
            temp = queue.popleft()
            if low<=temp<=high:
                result.append(temp)
            if temp > high:
                break 
            first_digit_right = temp % 10
            if first_digit_right == 9:
                continue
            element_to_push = (temp*10) +( first_digit_right+1)
            queue.append(element_to_push)
        return result