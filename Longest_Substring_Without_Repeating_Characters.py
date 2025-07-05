def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        x = s[right] 
        while x in seen:
            seen.remove(s[left])
            left += 1
        seen.add(x)
        max_length = max(max_length, right - left + 1)

    print(max_length)

lengthOfLongestSubstring("aaaaaabbbb")
lengthOfLongestSubstring("abcabcbb")



# Step-by-step explanation of how the function works for "aaaaaabbbb":

# right = 0, s[0] = 'a'
# 'a' is not in seen -> add it -> seen = {'a'}
# max_length = max(0, 0 - 0 + 1) = 1


# right = 1, s[1] = 'a'
# 'a' is in seen -> remove 'a' from seen -> left = 1
# Add 'a' again -> seen = {'a'}
# max_length = max(1, 1 - 1 + 1) = 1

# right = 2 to 5, all are 'a'
# Each time:
#   - 'a' is in seen -> remove 'a', move left forward
#   - Add 'a' again
#   - max_length stays 1

# right = 6, s[6] = 'b'
# 'b' is not in seen -> add it -> seen = {'a', 'b'}
# max_length = max(1, 6 - 5 + 1) = 2

# right = 7, s[7] = 'b'
# 'b' is in seen -> remove 'a' at left=5, then 'b', left = 7
# Add 'b' again -> seen = {'b'}
# max_length = max(2, 7 - 7 + 1) = 2

# right = 8, s[8] = 'b'
# Duplicate -> remove 'b', left = 8
# Add 'b' again -> seen = {'b'}
# max_length = 2

# right = 9, s[9] = 'b'
# Duplicate -> remove 'b', left = 9
# Add 'b' again -> seen = {'b'}
# max_length = 2

# ✅ Final Output: 2
# Longest substrings without repeating characters are:
# "a" → length = 1
# "ab" → length = 2