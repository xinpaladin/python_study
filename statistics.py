from random import randint

# 统计序列中元素的出现频度

data = [randint(0,10) for x in range(20)]
print('data :',data)

c = dict.fromkeys(data,0)

for x in data :
    c[x]+=1

print(c)
# 简洁方法

from collections import Counter

c2 = Counter(data)
print(c2.most_common(3))


# 统计英语词频

import re

txt = 'hello world hello world hello world hello world hello world '
c3 = Counter(re.split('\W+',txt))
print(c3.most_common(3))