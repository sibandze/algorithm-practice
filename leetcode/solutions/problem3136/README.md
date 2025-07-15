LeetCode 3136 "Valid Word"
-----

### **Algorithm Analysis: Valid Word**

This problem defines a "valid word" based on four criteria:

1.  Minimum length of 3 characters.
2.  Contains only digits (0-9) and English letters (a-z, A-Z).
3.  Includes at least one vowel.
4.  Includes at least one consonant.

We are given a string `word` and need to return `True` if it's valid, `False` otherwise.

#### **Core Idea: Regular Expressions and Character Set Checks**

The criteria lend themselves well to validation using regular expressions, particularly for character set validation and existence of specific character types (vowels/consonants). Length check is a simple string property.

#### **Step-by-Step Algorithm**

The solution directly translates the four validation criteria into a series of logical `AND` conditions. All conditions must be true for the word to be considered valid.

1.  **Length Check:**

      * `len(word) >= 3`: This directly checks the first criterion. If the word has fewer than 3 characters, the entire expression will short-circuit to `False`.

2.  **Character Set Validation (Digits and English Letters Only):**

      * `re.match("^[a-zA-Z0-9]+$", word)`:
          * `re.match()`: Attempts to match the pattern only at the beginning of the string.
          * `^`: Asserts the start of the string.
          * `[a-zA-Z0-9]`: Character set matching any English letter (uppercase or lowercase) or any digit.
          * `+`: Matches one or more occurrences of the preceding character set.
          * `$`: Asserts the end of the string.
          * **Purpose:** This regular expression ensures that the *entire* string consists *only* of alphanumeric characters. If `re.match` finds a match, it returns a match object (which evaluates to `True` in a boolean context); otherwise, it returns `None` (evaluates to `False`).

3.  **Vowel Existence Check:**

      * `re.search("[aeiouAEIOU]", word)`:
          * `re.search()`: Scans through the string looking for *any* location where the pattern matches.
          * `[aeiouAEIOU]`: Character set matching any uppercase or lowercase English vowel.
          * **Purpose:** This checks if at least one vowel (case-insensitive) is present anywhere in the `word`. If `re.search` finds a match, it returns a match object (evaluates to `True`); otherwise, `None` (evaluates to `False`).

4.  **Consonant Existence Check:**

      * `re.search("[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]", word)`:
          * Similar to the vowel check, but uses a character set explicitly listing all English consonants (uppercase and lowercase).
          * **Purpose:** This checks if at least one consonant (case-insensitive) is present anywhere in the `word`.

#### **Return Value:**

  * The `return True` statement is executed only if *all four* conditions linked by `and` are met.
  * Otherwise, `return False` is executed.

#### **Example Trace (`word = "Leetcode2024"`)**

1.  `len(word) >= 3`: `len("Leetcode2024")` is `12`, `12 >= 3` is `True`.
2.  `re.match("^[a-zA-Z0-9]+$", "Leetcode2024")`: Matches successfully (contains only letters and digits). `True`.
3.  `re.search("[aeiouAEIOU]", "Leetcode2024")`: Contains 'e', 'o'. Matches. `True`.
4.  `re.search("[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]", "Leetcode2024")`: Contains 'L', 't', 'c', 'd', etc. Matches. `True`.

Since all conditions are `True`, the function returns `True`.

#### **Example Trace (`word = "123"`)**

1.  `len(word) >= 3`: `len("123")` is `3`, `3 >= 3` is `True`.
2.  `re.match("^[a-zA-Z0-9]+$", "123")`: Matches successfully. `True`.
3.  `re.search("[aeiouAEIOU]", "123")`: No vowels. Returns `None` (evaluates to `False`).

Since one condition is `False`, the entire expression evaluates to `False`, and the function returns `False`.

#### **Complexity Analysis**

Let $L$ be the length of the input `word`.

  * **Time Complexity:** $O(L)$

      * `len(word)` is $O(L)$.
      * `re.match("^[a-zA-Z0-9]+$", word)`: In the worst case, the regex engine might have to scan the entire string once. This is $O(L)$.
      * `re.search("[aeiouAEIOU]", word)`: In the worst case (no vowels or vowel at the very end), the regex engine might have to scan the entire string once. This is $O(L)$.
      * `re.search("[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]", word)`: Similarly, this is $O(L)$.
      * Since these operations are performed sequentially, the dominant factor is $O(L)$.

  * **Space Complexity:** $O(1)$ (excluding the space for the input string and the compiled regex patterns themselves, which are constant relative to `L`).

      * The regular expression engine might use some internal state, but it's generally considered constant auxiliary space for these types of simple patterns.

#### **Advantages of this Algorithm**

  * **Concise and Pythonic:** The use of `re` module makes the code very short and directly expresses the validation rules.
  * **Readable:** Regular expressions, once understood, provide a clear way to define character constraints.
  * **Efficient:** For typical string lengths, regular expression engines are highly optimized and perform very well.
  * **Robust:** Correctly handles case sensitivity for letters in validation.

#### **Alternative (Manual Iteration) Approach**

An alternative would be to manually iterate through the string and check each character:

```python
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False
        vowels = "aeiouAEIOU"
        
        for char_code in word:
            if 'a' <= char_code <= 'z' or 'A' <= char_code <= 'Z':
                if char_code in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
            elif not ('0' <= char_code <= '9'): # Not a letter, not a digit -> invalid char
                return False
        
        return has_vowel and has_consonant
```

This manual approach would have similar $O(L)$ time complexity (one pass) and $O(1)$ space complexity. It avoids regular expressions, which I sometimes find tricky myself.
