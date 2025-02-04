data = [
    {
        'name': 'galaxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galaxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galaxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.

for dict in data:
    for key in key_list:
        dict[key] = dict.get(key, 'unknown')

    for i in range(len(dict)):
        print(f'{key_list[i]}은/는 {dict[key_list[i]]}입니다.')
