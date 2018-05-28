
# 如何为元祖中的每个元素命名，提高程序可读性

# ('jim',16,'male','jim@163.com')
# ('jim1',17,'female','jim1@163.com')
# ('jim2',18,'male','jim2@163.com')

student = ('jim',16,'male','jim@163.com')
NAME,AGE,SEX,EMAIL = range(4) #感觉很鸡肋

print(student[NAME])
print(student[AGE])
print(student[SEX])
print(student[EMAIL])

# 使用namedtuple 替换 tuple

from collections import namedtuple
Student = namedtuple('Student',['name','age','sex','email'])
student1 = Student('jim1',17,'female','jim1@163.com')
student2 = Student(name ='jim1',age = 17,sex = 'female',email ='jim1@163.com')

print(student1.name)
print(student1.age)
print(student1.sex)
print(student1.email)