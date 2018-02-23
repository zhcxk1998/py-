import numpy as np

#   FFT操作
print(np.fft.fft(np.array([1,1,1,1,1,1,1,1])))#8点fft
print(np.corrcoef([1,0,1],[0,2,0])) #打印相关系数,皮尔逊相关系数计算
print(np.poly1d([2,1,3]))  #生成一元多次函数 2x**2 + 1x + 3 ,他生成一元二次函数