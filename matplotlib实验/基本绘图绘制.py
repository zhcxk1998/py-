import matplotlib.pyplot as plt
import numpy as np


#   绘制line
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
#              起点 终点 点的个数 是否包含终点
c = np.cos(x)
s = np.sin(x)
plt.figure(1)
#   plot(自变量,因变量,color颜色,linewidth线粗细,线形状,label标签,alpha透明度)
plt.plot(x, c, color="red", linewidth=1.0, linestyle="-", label="COS", alpha=0.5)
plt.plot(x, s, "b*", label="SIN", alpha=0.5)
plt.title("COS & SIN")
# 显示坐标轴
# 轴的编辑器     plt.gca()
set =plt.gca()
# spines 是四周的边线，none代表隐藏
set.spines["right"].set_color("none")
set.spines["top"].set_color("none")
# 位置设置到数据域的 0 位置
set.spines["left"].set_position(("data",0))
set.spines["bottom"].set_position(("data",0))
plt.show()
