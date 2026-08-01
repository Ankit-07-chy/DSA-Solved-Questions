def range_addition(length: int, updates: list[list[int]]) -> list[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    n = length
    diff = [0]*n
    for start,end,val in updates:
        end = end + 1
        diff[start] += val 
        if end < n:
            diff[end]-=val 

    for i in range(1,n):
        diff[i] = diff[i-1] + diff[i]
    return diff 
    # return []

if __name__ == "__main__":
    length = int(input())
    updates = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = range_addition(length, updates)
    print(" ".join(map(str, res)))
