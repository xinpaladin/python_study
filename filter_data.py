from random import randint

# 如何在列表、字典、集合中根据条件筛选数据0

data = [randint(-10, 10) for i in range(10)]
# print('data: ', data)
# 解决方案

# 列表
# 1. filter函数
data_filter = filter(lambda x: x > 0, data)
# print(timeit f)
# print('data1:',list(data_filter))
# 2. 列表解析 消耗时间较少 首选
data_2 = [i for i in data if i >= 0]
# print('data_2: ',data_2)

# 字典
data_dict = {x: randint(0, 100) for x in range(1, 20)}
print('data_dict:', data_dict)

data_filter_dict = {k: v for k, v in data_dict.items() if v > 90}
print('data_filter_dict:', data_filter_dict)

# 集合
s = set(data)
print('set :', s)

s_filter = {x for x in s if x > 0}
print('s_filter :', s_filter)
