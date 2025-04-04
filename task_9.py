def longest_unique_substring(s):
    char_index = {}  # Dictionary to store the last index of characters
    left = 0  # Left pointer of the sliding window
    max_length = 0  # Stores the maximum length found

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1  # Move left pointer to avoid repetition
        
        char_index[s[right]] = right  # Update last index of character
        max_length = max(max_length, right - left + 1)  # Update max length

    return max_length


print(longest_unique_substring("abcabcbb"))  
print(longest_unique_substring("bbbbb"))    
print(longest_unique_substring("pwwkew"))   
