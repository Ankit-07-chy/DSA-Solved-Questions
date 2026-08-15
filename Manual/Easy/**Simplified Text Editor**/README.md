# **Simplified Text Editor**

## Difficulty: Easy

## Platform: Manual

## Problem Link
[View Problem](https://www.oahelper.in/question-with-editor/OTEwMDAwNTM1fDA?company_id=MTYzM3ww)

## Solved On
15 Aug 2026 at 12:45 pm



A tiny text editor holds a single line of text. The line starts out empty, and you are given a list of `q` operations to apply to it, in order.

There are three kinds of operation:

*   `INSERT <text>` — appends `<text>` to the end of the current line. `<text>` is a non-empty string of English letters.
*   `BACKSPACE` — erases the last character of the current line. If the line is already empty, this operation does nothing.
*   `UNDO` — reverts the most recent *successful* `INSERT` or `BACKSPACE`, putting the line back into the state it had just before that operation. If there is no such operation left to revert, this operation does nothing.

An operation is called *successful* when it actually changes the line. An `INSERT` is always successful, a `BACKSPACE` is successful only when the line is non-empty, and an `UNDO` is successful only when there is something left to revert.

An `UNDO` reverts an `INSERT` or a `BACKSPACE`, never another `UNDO` *(inferred — the source lists only `INSERT` and `BACKSPACE` as the operations an `UNDO` targets, so consecutive `UNDO`s walk further and further back through the edit history instead of redoing one another)*.

Report the contents of the line after all `q` operations have been applied.

**Input Format**

The first line contains a single integer `q` — the number of operations.

Each of the next `q` lines contains one operation, written exactly as `INSERT <text>`, `BACKSPACE`, or `UNDO`. In an `INSERT` line the keyword and the text are separated by a single space, and `<text>` itself contains no spaces. *(inferred — the source presents the operations as a list of strings and gives no stdin layout, so the house count-line-then-one-item-per-line convention is used)*

**Output Format**

Print a single line containing the final contents of the text.

If the final text is empty, print an empty line. *(inferred — the source says to return the final state and that state can legitimately be the empty string)*

**Constraints**

*   `1 <= q <= 18000`
*   Every operation is one of `INSERT <text>`, `BACKSPACE`, or `UNDO`.
*   `1 <= |text| <= 20`, and `text` consists only of English letters (`a - z` and `A - Z`). *(inferred — the source caps the text at 20 English letters but does not forbid an empty one; empty text is excluded because it would make an `INSERT` change nothing, which the source's own definition of a successful operation does not cover)*
*   The sum of `|text|` over all `INSERT` operations is at most `17000`, so the final text never exceeds `17000` characters. *(inferred — the source states no total-size bound; this one keeps the printed answer inside the grader's output limit)*
*   All values fit comfortably in a 32-bit integer, so 64-bit arithmetic is **not** required; the answer is a string, not a number. *(inferred from the bounds above)*

**Examples**

**Example 1**

**Input:**
```
4
INSERT hello
INSERT world
BACKSPACE
UNDO
```

**Output:**
```
helloworld
```

## My Notes / Approach:
