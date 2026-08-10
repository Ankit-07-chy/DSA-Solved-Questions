# Longest Common Substring

## Difficulty: Medium

## Platform: GeeksForGeeks

## Problem Link
[View Problem](https://www.geeksforgeeks.org/problems/longest-common-substring1452/1)

## Solved On
10 Aug 2026 at 08:04 pm

<h2><a href="https://www.geeksforgeeks.org/problems/longest-common-substring1452/1">Longest Common Substring</a></h2><h3>Difficulty Level: Medium</h3><hr><p><span style="font-size: 18px;">Given two strings <strong>s1</strong> and <strong>s2</strong>, determine the length of the <strong>longest substring</strong> that appears in both strings.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>s1 = "ABCDGH", s2 = "ACDGHR"
<strong>Output:</strong> 4
<strong>Explanation</strong>: The longest common substring is "CDGH" with a length of 4.</span>
</pre>
<pre><span style="font-size: 18px;"><strong>Input</strong>: s1 = "abc", s2 = "acb"
<strong>Output:</strong> 1
<strong>Explanation</strong>: The longest common substrings are "a", "b", "c" all having length 1.
</span></pre>
<pre><span style="font-size: 18px;"><strong style="font-size: 18px;">Input</strong><span style="font-size: 18px;">: s1 = "YZ", s2 = "yz"
</span><strong style="font-size: 18px;">Output:</strong><span style="font-size: 18px;"> 0<br><strong>Explanation: </strong></span></span><span style="font-size: 18px;">Comparison is case-sensitive, so 'Y' ≠ 'y' and 'Z' ≠ 'z'. Hence, no common substring exists.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1&nbsp;<span style="font-size: 18.6667px;">≤</span>&nbsp;s1.size(), s2.size()&nbsp;<span style="font-size: 18.6667px;">≤</span>&nbsp;10<sup>3</sup><br>Both strings consist only of uppercase and lowercase English letters.</span></p>