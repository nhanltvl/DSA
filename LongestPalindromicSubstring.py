# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
# Ghi chú:
# - Đây là ví dụ minh họa đề bài "Longest Palindromic Substring".
# - Đầu vào là chuỗi s, đầu ra là một chuỗi con là palindrome dài nhất.
# - Trong ví dụ 1 cả "bab" và "aba" đều hợp lệ; bài toán có thể trả về bất kỳ đáp án nào trong số đó.
#
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
#
# Ghi chú:
# - Ví dụ 2 minh họa trường hợp có palindrome chẵn độ dài ("bb").

def longest_palindromic_substring(s: str) -> str:
    """
    Trả về chuỗi con palindrome dài nhất trong s.
    Thuật toán: kiểm tra mọi "tâm" (center) và mở rộng ra hai phía.
    """
    # Nếu chuỗi rỗng thì trả về chuỗi rỗng ngay
    if len(s) == 0:
        return ""

    # start, end lưu chỉ số biên trái/phải của palindrome dài nhất tìm được
    start, end = 0, 0

    # Duyệt từng vị trí i làm tâm
    for i in range(len(s)):
        # len1: độ dài palindrome lẻ khi tâm là i
        len1 = expand_around_center(s, i, i)      # Odd length palindromes
        # len2: độ dài palindrome chẵn khi tâm nằm giữa i và i+1
        len2 = expand_around_center(s, i, i + 1)  # Even length palindromes
        # chọn độ dài lớn hơn giữa lẻ và chẵn
        max_len = max(len1, len2)

        # Nếu tìm được palindrome dài hơn hiện tại thì cập nhật start/end
        if max_len > end - start:
            # Chuyển từ (i, max_len) -> biên start và end của palindrome
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    # Trả về chuỗi con từ start đến end (bao gồm)
    return s[start:end + 1]

def expand_around_center(s: str, left: int, right: int) -> int:
    """
    Mở rộng từ hai chỉ số left, right ra hai phía miễn là ký tự hai bên bằng nhau.
    Trả về độ dài palindrome tìm được.
    """
    # Mở rộng đến khi vượt biên hoặc ký tự không khớp
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # right - left - 1 cho độ dài của đoạn hợp lệ cuối cùng
    return right - left - 1

# Thêm test case để chạy nhanh bằng python3 LongestPalindromicSubstring.py
if __name__ == "__main__":
    tests = [
        ("babad", "Ví dụ: nhiều đáp án hợp lệ (\"bab\" hoặc \"aba\")"),
        ("cbbd", "Ví dụ: palindrome chẵn độ dài 'bb'"),
        ("a", "Chuỗi 1 ký tự"),
        ("", "Chuỗi rỗng"),
        ("forgeeksskeegfor", "Chuỗi có palindrome dài ở giữa"),
    ]

    for s, note in tests:
        res = longest_palindromic_substring(s)
        print(f"Input: {s!r}  -> Longest palindrome: {res!r}  ({note})")