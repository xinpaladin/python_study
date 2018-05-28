import re

# 调整字符串中文本的格式

'''
log文件，修改日期格式

2018-04-10 
'''

log = open('./output.log').read()

result = re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',log)
result1 = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<month>/\g<day>/\g<year>',log)
print(result)
print(result1)