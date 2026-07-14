# Insert At The Front of a Doubly Linked List

## Difficulty: Easy

## Platform: Manual

## Problem Link
[View Problem](https://www.naukri.com/code360/problems/insert-at-the-front-of-a-doubly-linked-list_9697366?leftPanelTabValue=PROBLEM)

## Solved On
14 Jul 2026 at 08:50 pm

Problem statement
You are given a doubly-linked list of length ‘n’.



You must insert a node having the value ‘k’ in the front of the doubly linked list.



Note:
A doubly-linked list is a data structure that consists of sequentially linked records, and the nodes have reference to both the previous and the next nodes in the sequence of nodes.
For Example:
Input: Linked List: 4 <-> 10 <-> 3 <-> 5 and ‘k’ = 20

Output: Modified Linked List: 20 <-> 4 <-> 10 <-> 3 <-> 5

Explanation: A new node having value ‘k’ = 20 is inserted at the front of the linked list.


Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
4
4 10 3 5
20
Sample Output 1:
20 4 10 3 5
Explanation of sample input 1:-
Explanation: A new node having value ‘k’ = 20 is inserted at the front of the linked list.
Sample Input 2:
0

5
Sample Output 2:
5
Explanation Of Sample Input 2:
The linked list was empty. So the new node is the only node in the modified linked list.
Expected time complexity:
The expected time complexity is O(1).
Constraints:-
0 <= ‘n’ <= 10^5
1 <= Value in linked list node <= 10^9
1 <= ‘k’ <= 10^9



## My Notes / Approach:
