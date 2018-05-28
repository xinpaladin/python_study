from random import randint
from collections import OrderedDict
# 让字典保持有序
'''
实际案例：
编程竞赛系统：对选手解题计时，完成后将该选手解题时间记录到字典中，
{'a':(2.32),'b':(2.32),'c':(2.32),'e':(2.32)}
比赛结束后，按照排名打印选手成绩
'''

# s1 = {x: tuple(randint(0, 10)) for x in 'abcdef'}

# print(sorted(s1, key=getValue(s1)))


# def getValue(s):
#     return [x[1] for x in s]


# 使用orderDict
from time import time
player = list('abcdefgh')
records = OrderedDict()
start = time()
for i in range(8):
    input()
    p = player.pop(randint(0, 7 - i))
    end = time()
    print(i + 1, p, end - start)
    records[p] = [i+1,end - start]

# print(records)
for record in records:
    print(record,records[record])