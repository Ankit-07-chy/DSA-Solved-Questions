# Consistent Data

## Difficulty: Medium

## Platform: Manual

## Problem Link
[View Problem](https://www.oahelper.in/problems/MjAyfDA/consistent-data)

## Solved On
28 Jul 2026 at 07:51 pm

A sequence containing only 0s and 1s is called a consistent sequence if no adjacent values in the sequence are the same. For example (010101..) is a consistent sequence while (011) is not. You are allotted a simple task.

Given an integer N that represents the size of a consistent sequence starting with '\0\'.

Find out the number of consistent subsequences of the given sequence mod 10⁹ + 7.

Note: A subsequence is a sequence that can be derived from the given sequence by deleting zero or more elements without changing the order of the remaining elements.

Function Description
Complete the function `Consistent()`. This function takes the following parameter and returns the required answer:
- `N`: Represents the size of the sequence

Input Format for Custom Testing
Note: Use this input format if you are testing against custom input or writing code in a language where we don't provide boilerplate code.
- The first line contains an integer N representing the sequence's size.

Output Format
Print the number of consistent subsequences mod 10⁹ + 7.

Constraints
- 1 ≤ N ≤ 10⁶

Sample Test Case
Input:
3

Output:
6

Explanation
Assumption:
- N = 3

Approach:
- The given consistent sequence is [0,1,0]
- The number of consistent subsequences is 6 which are [0], [1], [0], [0,1], [1,0], [0,1,0]
- The corresponding indices sets are [0], [1], [2], [0,1], [1,2], [0,1,2]

Therefore we will return 6 as our answer.

## My Notes / Approach:
