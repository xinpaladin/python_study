from random import randint

# 在一个for语句中迭代多个可迭代对象


'''
案例：
1、语文数学英语分别存储在3个列表中，同时迭代三个列表，计算总分

2、4各班级，每班的成绩独立放在一个列表内，依次迭代4个表，统计4个班成绩高于90的人
'''

chinese = [randint(60,100) for _ in range(40)] 
english = [randint(60,100) for _ in range(40)] 
math = [randint(60,100) for _ in range(40)] 

# zip 
# 
total = [] 

for c,e,m in zip(chinese,english,math):
    total.append(c+e+m)
print(total)


# itertools.chain 将多个列表连接
from itertools import chain

e1 = [randint(60,100) for _ in range(40)] 
e2 = [randint(60,100) for _ in range(40)] 
e3 = [randint(60,100) for _ in range(40)] 
e4 = [randint(60,100) for _ in range(40)] 

count = 0
for s in chain(e1,e2,e3,e4):
    if s >=90:
        count+=1

print(count)