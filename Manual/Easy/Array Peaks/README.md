# Array Peaks

## Difficulty: Easy

## Platform: Manual

## Problem Link
[View Problem](https://www.oahelper.in/question-with-editor/OTEwMDAwNTM2fDA?company_id=MTYzM3ww)

## Solved On
12 Aug 2026 at 11:32 pm



You are given an array target of n integers. An element is a peak when it is strictly greater than each of its immediate neighbours.

The rules are:
* An element target[i] that is not an endpoint is a peak when target[i] > target[i-1] and target[i] > target[i+1] .
* The first element target[0] is a peak when it is strictly greater than its only neighbour target[1] .
* The last element target[n-1] is a peak when it is strictly greater than its only neighbour target[n-2] .

Report all peak elements, in the order in which they appear in target .

Input Format
The first line contains a single integer n — the number of elements.

The second line contains n space-separated integers target[0], target[1], ..., target[n-1] . (inferred — the source shows an array literal and gives no stdin layout, so the house size-line-then-data-line convention is used)

Output Format
Print k , the number of peak elements, on the first line.

If k > 0 , print the k peak values on the second line, space-separated, in their original order. If k = 0 , print nothing after the first line. (inferred — the source says "return an array"; the count line is added so that an empty result is still a well-formed, non-empty response)

Constraints
* 2 <= n <= 2700 (inferred — the source states no bounds; n >= 2 keeps every element with at least one neighbour, and the upper bound keeps a peak-dense answer inside the grader's 18 KB output limit)
* -10^9 <= target[i] <= 10^9 (inferred — the source says "integers" without a range; this is the usual 32-bit-safe band)
* Duplicate values are allowed.
* Every value and the count both fit in a 32-bit signed integer, so 64-bit arithmetic is not required. (inferred from the bounds above — no sums or products are formed)

## My Notes / Approach:
