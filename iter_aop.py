from itertools import islice

# 对迭代器做切片操作
f = open('statistics.py','rb')

# for line in f:
#     print(line)


# 使用标准库中itertools.islice,他能返回一个迭代对象切片的生成器
# islice(f,5,10)

for line in islice(f,5,10):
    print(str(line))