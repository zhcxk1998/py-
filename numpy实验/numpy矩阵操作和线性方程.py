from numpy.linalg import *
import numpy as np

#   矩阵操作
# print(np.eye(5))#   单位矩阵

# ls=np.array([[1,2],
#              [3,4]])

# print(inv(ls))#     逆矩阵
# print(ls.transpose())#  矩阵倒置
# print(det(ls))#     求行列式,1*4 - 2*3 = -2

#   特征值和特征向量
# print(eig(ls))#   第一个array表示特征值，第二个array表示特征向量

#   方程求解
# ls=np.array([[1,2],
#              [3,4]])
# y=np.array([[5,],[7,]])
#   解方程  x + 2y = 5
#          3x + 4y = 7
# 解得:     x = -3
#           y = 4
# print(solve(ls,y))