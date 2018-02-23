import numpy as np

#   打印两行三列的零数组
# print(np.zeros([2,3]))
#   打印三行五列的一数组
# print(np.ones([3,5]))

#   打印随机数

#   rand(a)←打印一个,rand(a,b)打印a行b列个
# print(np.random.rand(2,4))  #   打印两行四列均匀分布随机数
# print(np.random.rand()) #    打印一个均匀分布的随机数

#   randint(a,b,c),a是起始，b是结束，c是个数
# print(np.random.randint(1,100))#    打印一个1到100的随机数
# print(np.random.randint(1,20,3))#   打印三个1到20的随机数

#   randn()生成正态分布随机数
# print(np.random.randn())
# print(np.random.randn(2,3))

#   choice生成随机数，choice([1,2,3])←从数组之中随机选取作为随机数
# print(np.random.choice([1,2,3]))#   从数组之中随便选一个数
# a=[10,20,30]
# print(np.random.choice(a))