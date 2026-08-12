# Sensor Data Correction

## Difficulty: Easy

## Platform: Manual

## Problem Link
[View Problem](https://www.oahelper.in/problems/OTEwMDAwNTM3fDA/sensor-data-correction?company_id=MTYzM3ww)

## Solved On
12 Aug 2026 at 11:15 pm


A logger writes its readings into one long string sensorReadings made of numbers separated by single spaces.

A reading is considered suspect when it contains at least one pair of equal digits standing next to each other. Every suspect reading must be replaced by the sum of its digits. Readings without such a pair are left exactly as they are.

Report the corrected string: the same readings, in the same order, separated by single spaces.

Input Format
A single line containing sensorReadings — one or more numbers separated by single spaces, with no leading or trailing spaces. (inferred — the source describes the input as one string of space-separated integers but gives no stdin layout)

Output Format
Print a single line: the corrected string, with the numbers in their original order and separated by single spaces.

Constraints
* 1 ≤ L ≤ 17000 , where L is the length of sensorReadings . (inferred — the source states no bound; this one keeps the corrected string, which is never longer than the input, inside the grader's 18 KB output limit)
* Every reading is a non-negative integer written with 1 to 18 decimal digits and no leading zeros, except for the reading 0 itself, which is the single character "0". (inferred — the source calls them "integers" and shows only non-negative values with no sign and no leading zeros; the 18-digit ceiling keeps every reading inside a signed 64-bit integer)
* The readings are separated by exactly one space, and there is at least one reading.
* A reading can be as large as 10^18 - 1, so parsing one into a 64-bit integer type is required; a 32-bit int overflows. The sum of the digits of a reading is at most 162 and needs no wide type at all. (inferred from the digit bound above)
* The intended solution runs in O(L) time. (stated by the source)

Examples
Example 1
Input:
123 4558 787

Output:
123 22 787

Explanation: 123 has no two equal digits next to each other, so it survives. 4558 contains the pair 55, so it becomes 4 + 5 + 5 + 8 = 22. 787 repeats the digit 7, but the two 7s are not adjacent, so it survives.

Example 2
Input:
0 11 909 1000

Output:
0 2 909 1

Explanation: 0 has a single digit and therefore no pair. 11 becomes 1 + 1 = 2. 909 repeats 9, but not in adjacent positions. 1000 contains 00, so it becomes 1 + 0 + 0 + 0 = 1.

Example 3
Input:
999999999999999999

Output:
162

Explanation: eighteen nines, so the very first two digits already form a pair, and the reading is replaced by 18 * 9 = 162.

## My Notes / Approach:
