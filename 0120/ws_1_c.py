password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."
# 아래에 코드를 작성하시오.

# 역순으로 슬라이싱을 진행하는 경우
# 시작점이 끝점보다 값이 커야 함

# 66~68의 역순은 마지막 숫자를 앞에 두고 66번째까지이므로 -1을 하기
# 반대로 322번째부터 4글자를 구하고 싶을 땐
# 322~325이므로 [325:322-1:-1]
# 의 형식으로 해주면 됨

first_char = password[28:36]
second_word = password[113:118]
third_word = password[68:65:-1]
fourth_word = password[325:321:-1]
fifth_word = password[365:371]

print(f'{first_char}{second_word} {third_word} {fourth_word} "{fifth_word}".')