import os, stat

# 判断字符串a是否以字符串b开头或结尾

# 

files = os.listdir('.')
print(files)
names = [name for name in files if name.endswith(('.py','.h'))]
print(names)