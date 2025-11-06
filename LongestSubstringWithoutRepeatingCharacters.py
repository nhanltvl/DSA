def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

if __name__ == "__main__":
    # Test case 1
    s1 = "abcabcbb"
    result1 = lengthOfLongestSubstring(s1)
    print(f"Test 1: Chuỗi = \"{s1}\"")
    print(f"Độ dài chuỗi con dài nhất không lặp lại: {result1}")
    print()

    # Test case 2
    s2 = "bbbbb"
    result2 = lengthOfLongestSubstring(s2)
    print(f"Test 2: Chuỗi = \"{s2}\"")
    print(f"Độ dài chuỗi con dài nhất không lặp lại: {result2}")
    print()

    # Test case 3
    s3 = "pwwkew"
    result3 = lengthOfLongestSubstring(s3)
    print(f"Test 3: Chuỗi = \"{s3}\"")
    print(f"Độ dài chuỗi con dài nhất không lặp lại: {result3}")
    print()

    # Test case 4
    s4 = ""
    result4 = lengthOfLongestSubstring(s4)
    print(f"Test 4: Chuỗi = \"{s4}\"")
    print(f"Độ dài chuỗi con dài nhất không lặp lại: {result4}")
    print()

    # Test case 5
    s5 = "aab"
    result5 = lengthOfLongestSubstring(s5)
    print(f"Test 5: Chuỗi = \"{s5}\"")
    print(f"Độ dài chuỗi con dài nhất không lặp lại: {result5}")
    print()
