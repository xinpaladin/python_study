

# 使用生成器函数实现可迭代对象

'''
实现一个可迭代对象的类，他能迭代出给定范围内所有素数
'''

# 生成器函数 包含yield
# 
class PrimeNum:
    def __init__(self,start,end):
        self.start = start 
        self.end = end

    def isPrimeNum(self,k):
        if k<2:
            return False
        for i in range(2,int(k/2)+1):
        # for i in range(2,k):
            if k%i == 0 :
                return False
        
        return True

    def __iter__(self):
        for k in range(self.start,self.end+1):
            if(self.isPrimeNum(k)):
                yield k


a = PrimeNum(0,30)
for i in a :
    print(i)