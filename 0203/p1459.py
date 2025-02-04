# 아래 클래스를 수정하시오.
class StringRepeater:
    def repeat_string(self, number, string):
        for _ in range(number):
            print(string)


repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
