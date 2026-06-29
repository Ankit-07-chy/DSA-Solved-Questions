class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        
        occupiedIntervals.sort(key=lambda x: x[0])  # FIXED: sort by start time

        result = []
        n = len(occupiedIntervals)

        def check_touch_overlap(pre_x, pre_y, curr_x, curr_y):
            if pre_y - curr_x == -1:  # touch condition: pre_y + 1 == curr_x
                return True, [pre_x, curr_y] 
            # Overlap conditions
            elif curr_x <= pre_x <= curr_y or curr_x <= pre_y <= curr_y or pre_x <= curr_x <= pre_y or pre_x <= curr_y <= pre_y:
                return True, [min(pre_x, curr_x), max(pre_y, curr_y)]
            return False, []
                
        for i in range(n):
            if result:
                pre_x, pre_y = result.pop()
                curr_x, curr_y = occupiedIntervals[i][0], occupiedIntervals[i][1]
                temp, new_interval = check_touch_overlap(pre_x, pre_y, curr_x, curr_y)
                if temp:
                    result.append(new_interval)
                else:
                    result.append([pre_x, pre_y])
                    result.append([curr_x, curr_y])
            else:
                result.append(occupiedIntervals[i])

        # Filter out free interval [freeStart, freeEnd]
        m = []
        for interval in result:
            x, y = interval[0], interval[1]
            
            # Case 1: No overlap - interval is completely outside free period
            if y < freeStart or x > freeEnd:
                m.append(interval)
            
            # Case 2: Complete overlap - free period covers entire interval
            elif x >= freeStart and y <= freeEnd:
                continue  # Skip this interval entirely
            
            # Case 3: Partial overlap - need to split the interval
            else:
                # Left part exists if interval starts before free period
                if x < freeStart:
                    m.append([x, freeStart - 1])
                # Right part exists if interval ends after free period
                if y > freeEnd:
                    m.append([freeEnd + 1, y])
        
        return m