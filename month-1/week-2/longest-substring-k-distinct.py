"""Find the length of the longest substring with at most K distinct characters."""


def longest_substring_k_distinct(s, k):
    char_count = {}
    left = max_len = 0

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# Example
print(longest_substring_k_distinct("eceba", 2))  # Output: 3 ("ece")
