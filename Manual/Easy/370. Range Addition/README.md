# 370. Range Addition

## Difficulty: Easy

## Platform: Manual

## Problem Link
[View Problem](https://algo.monster/liteproblems/370)

## Solved On
01 Aug 2026 at 11:37 pm

Problem Description
You start with an array of zeros with a given length. You're given a series of updates where each update is a triplet [startIdx, endIdx, inc] that tells you to:

Add inc to every element from index startIdx to endIdx (inclusive)
Your task is to apply all these updates to the array and return the final result.

Example walkthrough:

If length = 5 and updates = [[1, 3, 2], [2, 4, 3]]
Start with: [0, 0, 0, 0, 0]
After first update (add 2 to indices 1-3): [0, 2, 2, 2, 0]
After second update (add 3 to indices 2-4): [0, 2, 5, 5, 3]
Return: [0, 2, 5, 5, 3]
The challenge is to find an efficient way to handle potentially many updates without actually iterating through each range for every update, which would be inefficient. The solution uses a difference array technique:


## My Notes / Approach:

Instead of updating ranges directly, mark the boundaries:

When adding c to range [l, r], mark d[l] += c (start of increase)
Mark d[r+1] -= c (end of increase) if r+1 is within bounds
After marking all boundaries, compute the prefix sum of this difference array to get the final result. The prefix sum naturally propagates the increments across the ranges.

This approach reduces the time complexity from O(n × m) for naive range updates to O(n + m) where n is the array length and m is the number of updates.