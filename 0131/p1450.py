# 아래 함수를 수정하시오.
def get_keys_from_dict(dict):
    key = dict.keys()
    key_list = list(key)
    return key_list

def get_all_keys_from_dict(dictionary):
    lst = []
    for key1, value1 in dictionary.items():
        lst.append(key1)
        while type(value1) == dict:    
            for key2, value2 in value1.items():
                lst.append(key2)
                value1 = value2
    return lst

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

my_dict = {'person': {'name': 'Alice', 'age': 25}, 'location': 'NY'}
result = get_all_keys_from_dict(my_dict)
print(result)  # ['person', 'name', 'age', 'location']


