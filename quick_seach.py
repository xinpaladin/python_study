from random import randint, sample
from functools import reduce
# 快速查找多个字典中的公共键
'''
案例
足球联赛，每轮球员进球统计：
第1轮： {'a':1,'b':2,'c':3,...,'z':2}
第2轮： {'a':1,'b':2,'c':3,...,'z':2}
第3轮： {'a':1,'b':2,'c':0,...,'z':2}
统计前N轮，每场比赛都有进球的球员
'''

# 产生进球球员，sample随机取样
# a = sample('abcdef',3)

# b = sample('abcdef',randint(3,6))

s1 = {x: randint(1, 4) for x in sample('abcdef', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcdef', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcdef', randint(3, 6))}
print('s1: ', s1)
print('s2: ', s2)
print('s3: ', s3)
# 传统方法
res = []
for k in s1:
    if k in s2 and k in s3:
        res.append(k)

print('result:', res)

# 使用字典keys()方法，去到keys ，然后取交集
print(s1.keys() & s2.keys() & s3.keys())

# map reduce
# 案例集合为3 ，N轮

a = map(lambda x: x.keys(), [s1, s2, s3])
d = reduce(lambda a, b: a & b, map(lambda x: x.keys(), [s1, s2, s3]))
print('map reduce result:', d)
