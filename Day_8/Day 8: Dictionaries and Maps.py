n = int(input().strip())

phoneBook = {}
for i in range(n):
    add_value = [str(arr_temp) for arr_temp in input().strip().split(' ')]
    phoneBook[add_value[0]] = add_value[1]

for j in range(n):
    key_value = str(input().strip())
    if key_value in phoneBook:
        print('{}={}'.format(key_value, phoneBook[key_value]))
    else:
        print('Not found')