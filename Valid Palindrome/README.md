# LeetCode 125 - Valid Palindrome

## Problem Statement

Given a string `s`, determine whether it is a palindrome after:

- Converting all uppercase letters to lowercase.
- Removing all non-alphanumeric characters.

Return `true` if the resulting string is a palindrome; otherwise, return `false`.

**LeetCode Link:** https://leetcode.com/problems/valid-palindrome/

---

## Approach

This solution first constructs a cleaned version of the input string by:

- Ignoring all non-alphanumeric characters.
- Converting uppercase letters to lowercase.

After preprocessing, the cleaned string is compared with its reverse. If both are identical, the string is a valid palindrome.

---

## Algorithm

1. Initialize an empty string.
2. Traverse each character in the input string.
3. Keep only alphanumeric characters.
4. Convert each character to lowercase.
5. Compare the cleaned string with its reversed version.
6. Return the comparison result.

---

## Complexity Analysis

**Time Complexity:** `O(n)`

- Traversing the string takes `O(n)`.
- Reversing the string also takes `O(n)`.

**Space Complexity:** `O(n)`

- Additional space is used to store the cleaned string.

---

## Python Solution

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        return cleaned == cleaned[::-1]
```

---

## Example

### Input

```text
s = "A man, a plan, a canal: Panama"
```

### Output

```text
true
```

---

### Input

```text
s = "race a car"
```

### Output

```text
false
```

---

## Key Concepts

- Strings
- Two-Pass Processing
- Character Filtering
- String Manipulation
- Palindrome
- Python Built-in Methods

---

## Folder Structure

```text
Valid Palindrome/
│── ValidPalindrome.py
└── README.md
```

---

## Author

**Naveen Kushwaha**

GitHub: https://github.com/naveenkushwaha7804