def restructure_word(word, arr):
    for out in word:
        # for char in arr:
        if out.isdecimal() is True:
            for _ in range(int(out)):
                arr.pop()
        elif out in arr:
            arr.remove(out)
    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
arr.extend(original_word)
print(arr)

result = restructure_word(word, arr)
print(result)


result_2 = "".join(arr)

print(result_2)