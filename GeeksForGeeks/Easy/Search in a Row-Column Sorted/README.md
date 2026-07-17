# Search in a Row-Column Sorted

## Difficulty: Easy

## Platform: GeeksForGeeks

## Problem Link
[View Problem](https://www.geeksforgeeks.org/problems/search-in-a-matrix17201720/1)

## Solved On
17 Jul 2026 at 12:10 pm

<h2><a href="https://www.geeksforgeeks.org/problems/search-in-a-matrix17201720/1">Search in a Row-Column Sorted</a></h2><h3>Difficulty Level: Easy</h3><hr><p><span style="font-size: 14pt;">Given a 2D integer matrix <strong>mat[][]</strong> of size <strong>n x m</strong>, where every row and column is sorted in increasing order and a number <strong>x</strong>, return <strong>true </strong>if the element <strong>x</strong> is present in the matrix. Otherwise, return <strong>false</strong>.</span></p>
<p><strong><span style="font-size: 14pt;">Examples:</span></strong></p>
<pre><span style="font-size: 14pt;"><strong>Input</strong>: mat[][] = [[3, 30, 38], [20, 52, 54], [35, 60, 69]], x = 62
<strong>Output</strong>: false
<strong>Explanation</strong>: 62 is not present in the matrix, so output is false.<br></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input</strong>: mat[][] = [[18, 21, 27],  [38, 55, 67]], x = 55
<strong>Output</strong>: true
<strong>Explanation</strong>: 55 is present in the matrix.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input</strong>: mat[][] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], x = 3
<strong>Output</strong>: true
<strong>Explanation</strong>: 3 is present in the matrix.<br></span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints</strong>:<br>1&nbsp;<span style="color: #273239; font-family: Nunito; font-size: 17px; background-color: #ffffff;">≤</span>&nbsp;n, m&nbsp;<span style="color: #273239; font-family: Nunito; font-size: 17px; background-color: #ffffff;">≤ </span>10<sup>3</sup><br>1&nbsp;<span style="color: #273239; font-family: Nunito; font-size: 17px; background-color: #ffffff;">≤</span>&nbsp;mat[i][j]&nbsp;<span style="color: #273239; font-family: Nunito; font-size: 17px; background-color: #ffffff;">≤</span>&nbsp;10<sup>9 <br></sup>1 <span style="color: #273239; font-family: Nunito; font-size: 17px; background-color: #ffffff;">≤</span>&nbsp;x&nbsp;<span style="color: #273239; font-family: Nunito; font-size: 17px; background-color: #ffffff;">≤</span>&nbsp;10<sup>9</sup></span></p>