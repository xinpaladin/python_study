

# 拼接字符串

# 方法1 ： 使用 + 
# 方法2 ： 使用 str.join()

a = ';'.join(['asdsda','asdasd','1111'])
l = ['asdsda','asdasd',333,123123]
a1 = ';'.join(str(x) for x in l)
# print(a)
# print(a1)

# 对字符串 进行左中右对齐

# 方法1: 使用 str.ljust()
s = 'abc'

print(s.ljust(20,'-'))
print(s.rjust(20,'-'))

# 方法2： format

print(format(s,'<20'))
print(format(s,'>20'))
print(format(s,'^20'))

# 去掉字符串中不需要的字符