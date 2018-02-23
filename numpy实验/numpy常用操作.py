import numpy as np

# #   生成等差数列，arange(x,y)指的是[x,y)
# print(np.arange(1,11))
# #   通过reshape将等差数列变成x行y列状
# print(np.arange(1,11).reshape(10,1))
# print(np.arange(1,11).reshape(2,5))

#   对array数组进行各种操作
# ls = np.arange(1, 11).reshape(5, 2)
# print(ls)
# print(np.exp(ls))
# print(np.sin(ls))
# print(np.sqrt(ls))
# print(np.log(ls))

#   sum求和
# print(ls.sum())#    所有元素相加
# print(ls.sum(axis=0))#  axis越小，代表深入程度越小
# print(ls.sum(axis=1))
# 应该是对于二维矩阵而言, sum函数里面的axis是指定行或者列.
# axis=0的话是按列求和, axis=1是按行求和
# 如果没有axis参数的话就是全部元素求和
# 更高维度的矩阵的话axis可以看成指定的是维度

list = np.array([[[1, 2, 3, 4],
                  [4, 5, 6, 7, ]],
                 [[7, 8, 9, 10],
                  [11, 12, 13, 14]],
                 [[15, 16, 17, 18],
                  [19, 20, 21, 22]]
                 ])
print(list.sum(axis=0))  # axis表示维度，axis=0,表示最外层的元素相加
print(list.sum(axis=1))  # 表示最外层减一层的元素相加
print(list.max(axis=0))  # 最外层元素中的最大元素值
print(list.min(axis=0))  # 最外层元素中的最小元素值
#--------------------------------------------------------------------------------

#   多个数组操作
ls1 = np.array([1, 2, 3, 4])
ls2 = np.array([10, 20, 30, 40])
# print(ls1+ls2)#     对应位置元素相加
# print(ls1*ls2)#     对应位置元素相乘
# print(ls1**2)#      乘方
# print(np.dot(ls1.reshape(2,2),ls2.reshape(2,2)))#   矩阵点乘
#   追加
#   np.concatenate((list1,list2))让list2追加在list1后
# print(np.concatenate((ls1,ls2)))#   数组追加
# print(np.vstack((ls1,ls2)))#        在新的一行追加,将两个数组分成两行组成一个数组也就是以行连接
# print(np.hstack((ls1,ls2)))#        数组追加
#   分隔
# print(np.split(ls1,2))#     将ls1分成2份
# print(np.split(ls2,4))#     将ls2分成4份
#   拷贝
# print(np.copy(ls1))

