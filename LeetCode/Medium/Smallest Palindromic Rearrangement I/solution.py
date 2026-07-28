class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        # lexicographically smallest palindrome
        if n <= 3:
            return s
        
        # able to findout every char occurance
        freq = {}
        for char in s:
            freq[char] = freq.get(char,0)+1

        # now sort this based on : ord : a - b - c ---- z
        start = []; end = []
        # we know that element which is either ord or having last in ord sorting can come in mid

        # start => .join(start) # end => reverse the end then join # > for middle if only odd occurace coming then mid will occupy
        # return -> start + mid + end
        # freq.items()
        freq = dict(sorted(freq.items(),key=lambda x:x[0]))
        # print(freq) # to check is it coming correctly or not
        
        mid = False
        for u,v in freq.items():
            if v % 2 == 1:
                mid = u 
            temp1 = u*(v//2)
            start.append(temp1)
            end.append(temp1)
        start = ''.join(start)
        end = ''.join(end)
        if mid:
            return start + mid + end[::-1]
        return start + end[::-1]