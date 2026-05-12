class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # applying Binary Search
        l = 0; r = 10**9
        tasks.sort(key=lambda x: x[1]-x[0], reverse=True) # much imp
        result = float('inf')
        def check(tasks,current_energy):
            temp = current_energy
            for i in range(len(tasks)):
                if tasks[i][1]> temp:
                    return False
                elif tasks[i][1] <= temp:
                    temp -= tasks[i][0]
            return True
        while l <= r:
            mid = (l+r)//2
            t = check(tasks,mid) # return true and false
            if t:
                result = min(result,mid)
                r = mid - 1
            else:
                l = mid + 1
        return result
"""
from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort tasks by the required energy (x[1]) in descending order
        tasks.sort(key=lambda x: x[1], reverse=True)

        min_energy = 0
        current_energy = 0

        for cost, required in tasks:
            # If current_energy is less than required, we need to increase min_energy
            if current_energy < required:
                # The deficit is (required - current_energy)
                # We need to add this deficit to min_energy
                min_energy += (required - current_energy)
                current_energy = required  # Reset current_energy to the required amount

            # Perform the task: subtract the cost
            current_energy -= cost

        # The total minimum energy is min_energy
        return min_energy
"""
'''
from typing import List
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # sort the tasks based on tasks --> t[1]; in decending order
        # tasks.sort(reverse=True, lambda x[1] : for x in tasks)
        tasks.sort(key=lambda x: x[1], reverse=True)
        # print(tasks)
        initial_energy = tasks[0][1]
        while True:
            curr_energy = initial_energy
            counter = 0; n = len(tasks)
            for i in range(n):
                print('ie:ce',initial_energy,curr_energy,counter)
                if tasks[i][1]<=curr_energy:
                    curr_energy -= tasks[i][0]
                    counter += 1
                elif tasks[i][1] > curr_energy:
                    initial_energy += (tasks[i][1]-curr_energy)
                    counter = 0
                    break
                if counter == n:
                    return initial_energy

                    '''