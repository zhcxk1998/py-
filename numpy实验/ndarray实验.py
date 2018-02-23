import numpy as np

a = [1, 2, 3]
c = [[1, 2, 3], [4, 5, 6]]
b = np.array(a)
d = np.array(c)

# print(type(a),type(b))

# c=np.array(a,dtype=int)   #设置数据类型

#   描述数组的形状
# print(b.shape)    #3个数据
# print(d.shape)    #两行三列

#   描述数组的维度
# print(b.ndim)   #一维
# print(d.ndim)   #二维

#   查看数组的数据类型
# print(b.dtype)
# print(d.dtype)

#   查看数组一个元素占用字节大小
# print(b.itemsize)
# print(d.itemsize)

#   查看数组元素多少,总字节数=b.size * b.itemsize
print(b.size)
print(d.size)
