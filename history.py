from random import randint
from collections import deque
import pickle
# 实现历史记录功能
# 显示用户最近猜过的数字（最多n条)


# deque 队列
# pickle 把python对象存到文件中，也可以存文件中读取对象
a = randint(0, 100)
history = deque([], 5)


def guess(b):
    if a == b:
        print('恭喜你猜中了, %s是正确的' % b)
        return True
    elif a > b:
        print('猜的数字 %s小了' % b)
    else:
        print('猜的数字 %s大了' % b)
    return False


while True:
    b = input()
    if b == 'h?' or b == 'history':
        print(list(history))
    else:
        history.append(b)
        if guess(int(b)):
            break

# pickle
# pickle.dump(history,open('history','w')) 报错write() argument must be str, not bytes
# 产生问题的原因是因为pickle存储方式默认是二进制方式
pickle.dump(history,open('history','wb'))
history2 = pickle.load(open('history','rb'))
print(history2)