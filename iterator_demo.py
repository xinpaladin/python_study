
# 实现可迭代对象和迭代器对象

'''
网络抓取 各个城市气温信息，并依次显示
北京：15~20
深圳：15~20
上海：15~20

一次性抓取所有城市天气再显示， 有延时 而且 浪费存储空间
'''

# 可迭代 ， 由可迭代对象 得到迭代器

l = [1,2,3,4,5]
# 列表 存在__iter__() 可返回得带其对象
# str 存在__getitem__()


# 迭代器对象 实现了 next()


from collections import Iterable,Iterator

class WeatherIterator(Iterator):
    '''
    可迭代对象
    '''
    def __init__(self,cities):
        self.cities = cities
        self.index = 0

    def getWeather(self,city):
        return '北京 20,35'

    def next(self):
        if self.index == len(self.cities)
            raise StopIteration
        city = self.cities[index]
        self.index+=1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    '''
        迭代器
    '''
    def __init__(self,cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)