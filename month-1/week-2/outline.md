# Array and String: Dynamic arrays, common string operations, sliding window technique (15 - 22 Jan).

Arrays and Strings are fundamental data structure for storing and manipulating collections of elements. Strings can be treated as immutable array of characters.

# Key Concepts

1. Dynamic Arrays

Dynamic arrays automatically resize when the elements are added beyond their current capacity.

- How they work:
  When the array's capacity is exceeded, a new array is created with double the capacity, and elements are copied over.

- operations:
  - Access: O(1)
  - Append: O(1) (amortized)
  - Insert/Delete: 0(n) (requires shifting elements)

In Python, the built-in `list` behaves as dynamic array.

2. Common String Operations

   - Concatenation: Combine strings (O(n)).
   - Slicing: Extract substrings (O(k), where k is the sliced length).
   - Searching: Check for substring (O(n+m), with advanced algorithms).
   - Replacing: Replace character or substring (O(n)).

3. Sliding Window Technique

The **Sliding Window Technique** is an optimization strategy used to reduce nested loop when working with contiguous sub-arrays or sub-strings.

- How It Works: <br />
  Maintain a "window" of elements and slide it over the array or string to compute result efficiently.

- Common Use Cases:
  - Maximum sum sub-arrays
  - Longest substring with specific constraint.
  - Anagram or permutation in a string.

# Why Are These Useful?

1. Arrays and strings provide the basis for many algorithms.
2. Understanding dynamic resizing helps optimize memory usage.
3. Sliding window reduces complexity for problems involving sub-arrays or sub-strings.

# When To Use These Concepts

1. When manipulating or analyzing contiguous (connected) data (e.g., substring, sub-array problems).
2. For problems requiring efficient memory usage (e.g., large datasets).
3. To replace brute-force solutions for sub-array or sub-string problems.

# Code Samples

1. Dynamic Array: See `dynamic-array.py` for code.

2. Common String Operation: See `common-string-operation.py`

3. Sliding Window Technique:
   - Finding the maximum size of sub-array of `K`. See `sliding-window-technique.py`
   - Longest sub-string with at most `k` distinct character. See `longest-substring-k-distinct.py`

# How To Analyze Complexity
**Dynamic Array**
- Appending: Amortized O(1) due to resizing.
- Resizing: O(n) when copying elements.

**String Operations**
- Concatenation: O(n) for n characters.
- Slicing: O(k) for k-length slice.
- Searching: O(n + m) using algorithms like KMP.

**Sliding Window**
- Iterates through the array once: O(n).
- Space complexity depends on auxiliary structures like dictionaries or sets.

# Practice Problem

Problem: Find all anagram of string a string `P` in string of `S`. See code `find-anagram.py`.
