# 아래 함수를 수정하시오.
def capitalize_words(words):
    word_lst = words.split()
    cap_words = []
    for word in word_lst:
        cap_words.append(word.capitalize())
    return ' '.join(cap_words) 
    


result = capitalize_words("hello, world!")
print(result)
