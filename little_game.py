from random import randint
from collections import deque
import pickle

# 
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