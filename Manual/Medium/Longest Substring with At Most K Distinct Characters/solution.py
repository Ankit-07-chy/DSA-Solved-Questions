def kDistinctChars(k, str):
    # Write your code here
    # Return an integer value
    
    left = 0; right = 0
    maxLen = 0; freq = {}
    for right in range(len(str)):
        freq[str[right]] = freq.get(str[right],0)+1
        while len(freq)>k:
            freq[str[left]] -= 1
            if freq[str[left]] == 0:
                freq.pop(str[left])
            
            left += 1
        maxLen = max(maxLen,right-left+1)
    return maxLen

