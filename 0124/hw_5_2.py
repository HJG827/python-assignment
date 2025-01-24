# 아래 함수를 수정하시오.
def count_character(words, letter):
    count = 0
    for char in words:
        if char == letter:
            count += 1
    return count


result = count_character("Hello, World!", "o")
print(result)  # 2
