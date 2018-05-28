from random import randint
# 根据字典中值的大小，对字典进行排序

data = [randint(0, 10) for x in range(20)]
print('data:', data)
print('sort data: ', sorted(data))

data_dict = {x: randint(60, 90) for x in 'abcdef'}
print('data_dict:',data_dict)

print('sorted function :',sorted(data_dict.items(),key=lambda x : x[1]))

# 
dict_zip = zip(data_dict.values(),data_dict.keys())
print('dict_zip:',list(dict_zip))
print('dict_zip:',dict_zip)
print('sort dict_zip1: ', sorted(zip(data_dict.values(),data_dict.keys())))
print('sort dict_zip2: ', sorted(dict_zip))

# 很迷惑
# sorted(zip(data_dict.values(),data_dict.keys())) 能正确打印
# 
# dict_zip = zip(data_dict.values(),data_dict.keys())
# print('sort dict_zip: ', sorted(dict_zip))

