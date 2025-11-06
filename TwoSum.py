# Đây là chương trình Python đầu tiên của bạn
def two_sum(numbers, target):
    num_dict = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_dict:
            return (num_dict[complement], i)
        num_dict[num] = i
    return None

# Test cases để chạy thử
if __name__ == "__main__":
    # Test case 1
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(numbers1, target1)
    print(f"Test 1: numbers = {numbers1}, target = {target1}")
    print(f"Kết quả: {result1}")
    if result1:
        print(f"Hai số tại vị trí {result1[0]} và {result1[1]} là: {numbers1[result1[0]]} + {numbers1[result1[1]]} = {target1}")
    print()
    
    # Test case 2
    numbers2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(numbers2, target2)
    print(f"Test 2: numbers = {numbers2}, target = {target2}")
    print(f"Kết quả: {result2}")
    if result2:
        print(f"Hai số tại vị trí {result2[0]} và {result2[1]} là: {numbers2[result2[0]]} + {numbers2[result2[1]]} = {target2}")
    print()
    
    # Test case 3
    numbers3 = [3, 3]
    target3 = 6
    result3 = two_sum(numbers3, target3)
    print(f"Test 3: numbers = {numbers3}, target = {target3}")
    print(f"Kết quả: {result3}")
    if result3:
        print(f"Hai số tại vị trí {result3[0]} và {result3[1]} là: {numbers3[result3[0]]} + {numbers3[result3[1]]} = {target3}")
    print()
    
    # Test case 4 - không có kết quả
    numbers4 = [1, 2, 3]
    target4 = 10
    result4 = two_sum(numbers4, target4)
    print(f"Test 4: numbers = {numbers4}, target = {target4}")
    print(f"Kết quả: {result4}")
    if result4:
        print(f"Hai số tại vị trí {result4[0]} và {result4[1]} là: {numbers4[result4[0]]} + {numbers4[result4[1]]} = {target4}")
    else:
        print("Không tìm thấy cặp số nào có tổng bằng target")
    print()