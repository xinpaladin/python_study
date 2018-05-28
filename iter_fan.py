# 如何反向迭代以及如何实现反向迭代
'''
案例
实现一个连续副段淑发生器FloatRange,根据给定的范围和步进产生一序列连续浮点数
FloatRange(3.0,4.0,0.2)
example: 3.0 -> 3.2-> 3.4-> 3.6-> 3.8-> 4.0  正向
example: 4.0 -> 3.8-> 3.6-> 3.4-> 3.2-> 3.0  反向
'''

# reversed(l) 得到反向迭代器
l = [1, 2, 3, 4, 5, 6]

for i in reversed(l):
    print(i)


class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end 
        while t>=self.start:
            yield t
            t -=self.step

for x in FloatRange(1.0,4.0,0.5):
    print('iter',x)

for y in reversed(FloatRange(1.0,4.0,0.5)):
    print('reversed ',y)