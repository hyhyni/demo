d = {'a':'apple', 'b':'banana', 'c':'car', 'd': 'desk'}

for key in d:
    # 遍历字典时遍历的是键
    print(key, d.get(key))