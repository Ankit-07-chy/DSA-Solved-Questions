# Longest Increasing Subsequence

## Difficulty: Medium

## Platform: GeeksForGeeks

## Problem Link
[View Problem](https://www.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1)

## Solved On
15 Jul 2026 at 11:05 am

<h2><a href="https://www.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1">Longest Increasing Subsequence</a></h2><h3>Difficulty Level: Medium</h3><hr><p><span style="font-size: 14pt;">Given an array <strong><code>arr[]</code></strong> of non-negative integers, the task is to find the <strong>length</strong> of the <strong>Longest Strictly Increasing Subsequence (LIS)</strong>.<br></span><span style="font-size: 14pt;">A subsequence is <strong>strictly increasing</strong> if each element in the subsequence is strictly less than the next element.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr<span class="hljs-selector-attr">[]</span> = <span class="hljs-selector-attr">[5, 8, 3, 7, 9, 1]</span>
<strong>Output: </strong>3<strong>
Explanation: </strong>The longest strictly increasing subsequence could be <code>[5, 7, 9]</code><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">, which has a length of 3.</span></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr[] = [10, 6, 3, 11, 7, 15]
<strong>Output: </strong>3<strong>
Explanation: </strong>One of the possible longest strictly increasing subsequences is <code>[10, 11, 15]</code><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">, which has a length of 3.</span></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr[] = [3, 10, 2, 1, 20]
<strong>Output: </strong>3<strong>
Explanation: </strong>The longest strictly increasing subsequence could be <code>[3, 10, 20]</code><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">, which has a length of 3.</span></span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong></span><br><span style="font-size: 14pt;">1 ≤ arr.size() ≤ 10<sup>3</sup><br>0 ≤ arr[i] ≤ 10<sup>6</sup></span></p>