"""Find all anagrams of a string P in a string S."""


def find_anagrams(s, p):
    from collections import Counter

    p_count = Counter(p)
    s_count = Counter(s[: len(p) - 1])
    result = []

    for i in range(len(p) - 1, len(s)):
        s_count[s[i]] += 1  # Include current char in window
        if s_count == p_count:
            result.append(i - len(p) + 1)

        # Remove the leftmost character from the window
        s_count[s[i - len(p) + 1]] -= 1
        if s_count[s[i - len(p) + 1]] == 0:
            del s_count[s[i - len(p) + 1]]

    return result


# Example
print(find_anagrams("cbaebabacd", "abc"))  # Output: [0, 6]
