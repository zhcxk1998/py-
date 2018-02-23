import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#   基本数据结构
# s=pd.Series([i*2] for i in range(1,11))
# dates = pd.date_range("20170301", periods=8)
# df = pd.DataFrame(np.random.randint(1, 100, (8, 5)), index=dates, columns=list('ABCDE'))

# -------------------------------------------------------------------------

#   基本操作
# print(df.head(3))#  打印前三行
# print(df.tail(3))#  打印后三行
#
# print(df.index)#    打印索引
# print(df.values)#   打印值

# print(df.T)#    矩阵倒置

# print(df.sort_values('C')) #第C列的values按从小到大的顺序排序
# print(df.sort_index(axis=1,ascending=False))#按索引进行降序排序

# print(df.describe())#数据描述

# -------------------------------------------------------------------------

# 选择，切片
# print(df['A'])# 打印出A列数据
# print(df[:4])#  打印出前4行数据
# print(df["20170301":"20170302"])#   打印出1号到2号之间的数据
# print(df.loc[dates[0]])#  读取第一行的数据
# print(df.loc["20170302":"20170305",["B","D"]])# 读取2号到5号之间的B和D列的数据
# print(df.at[dates[0],"C"])# 读取第一行C列的数据
# print(df.iloc[1:4,2:5])#    通过切片选择数据，总共 1到4（不包括4）行，2到5（不包括5）列
# print(df.iloc[0,0])#    打印第一行第一列的数据

# print(df[df>50])#   打印出大于50的值
# print(df[df.A>df.B])#   打印出A列大于B列的数据
# print(df[df.B>70])# 打印出B列大于70的数据
# print(df[df>50][df<60])#打印出50到60之间的数

# -------------------------------------------------------------------------

# 设置
# s1=pd.Series(list(range(10,18)),index=pd.date_range("20170301",periods=8))
# df['F']=s1#新增F列，数据是上面的10到17
# df.at[dates[0],"A"]=0#设置第一行A列的数据为0
# df.iat[1,1]=1#设置第二行第二列的值变为1
# df.loc[:,"D"]=np.array([4]*len(df))#将D列所有的值变成4
# print(df)

# df2=df.copy()#拷贝df
# df2[df2<60]=0#将小于60的数变为0
# print(df2)

# -------------------------------------------------------------------------

# 缺失值处理
# df1=df.reindex(index=dates[:4],columns=list("ABCD")+["G"])#取原数据前四行，并添加G列
# df1.loc[dates[0]:dates[1],"G"]=1#将前两行G列数据变为1
# print(df1)
# print(df1.dropna())#丢弃没有数据的行
# print(df1.fillna(value=0))#将没有数据的地方，填充为0

# -------------------------------------------------------------------------

# 表统计与整合
# print(df.mean())  # 获得均值
# print(df.var())  # 获得方差
# s = pd.Series([1, 2, 4, np.nan, 5, 7, 9, 10], index=dates)
# print(s)
# print(s.shift(2))  # 将数据往后移两位，数据推移，前两个数据将变为空值
# print(s.diff())  # 这里是代表，当前数据减去上一位数据的值
# print(s.value_counts())  # 打印每个数值的个数
# print(df.apply(np.cumsum))  # 表示引用求和“np.cumsum”函数，后面的值都是前面的累加
# print(df.apply(lambda x: x.max() - x.min()))  # 使用lambda函数求极差

# -------------------------------------------------------------------------

# 表格拼接
# pieces =[df[:3],df[-3:]]#构建前三行和后三行的集合
# print(pd.concat(pieces))#使用concat函数拼接

# left = pd.DataFrame({"key": ["x", "y"], "value": [1, 2]})
# right = pd.DataFrame({"key": ["x", "z"], "value": [3, 4]})
# print("LEFT:", left)
# print("RIGHT", right)
# print(pd.merge(left, right, on="key", how="left"))  #拼接key，拼接方式是保留left里包含的元素，
# print(pd.merge(left, right, on="key", how="inner"))
# print(pd.merge(left, right, on="key", how="outer"))

# df3=pd.DataFrame({"A":["a","b","c","b"],"B":list(range(4))})
# print(df3.groupby("A").sum())#A里的索引值相加

# -------------------------------------------------------------------------

# 时间序列
# t_exam=pd.date_range("20170301",periods=10,freq="s")#10个时间段，以“秒”区分
# print(t_exam)

# -------------------------------------------------------------------------

# 绘图操作
# from pylab import *
# ts=pd.Series(np.random.randint(1,1000,100),index=pd.date_range("20170301",periods=100))
# # ts=ts.cumsum()
# ts.plot()
# show()

# -------------------------------------------------------------------------

# 文件操作
# df6 = pd.read_csv("aa.csv")
# # print(df6)
# df7 =pd.read_excel("bb.xlsx")
# # print(df7)
# df6.to_csv("cc.csv")
# df7.to_excel("bb2.xlsx")

df = pd.read_excel("bb.xlsx")

df["SCORE2"] = np.random.randint(1, 101, len(df))
df["SCORE"] = np.random.randint(1, 101, len(df))
# df=df.set_index(['NUM'])
df['BLOCK'] = df.SCORE // 10 * 10
df['BLOCK2'] = df.SCORE2 // 10 * 10
df['SUM']=df.groupby('BLOCK')['BLOCK'].count()
df['SUM2']=df.groupby('BLOCK2')['BLOCK2'].count()

SUM=df.groupby('BLOCK')['BLOCK'].count()
SUM=SUM.reindex(range(0,209))
SUM2=df.groupby('BLOCK2')['BLOCK2'].count()
SUM2=SUM2.reindex(range(0,209))
# shuju=pd.DataFrame(SUM,index=range(0,208),columns='SUM')
df.loc[(df['SCORE']>=60)&(df['SCORE2']>=60),'TAG']='GOOD'#两次成绩都大于等于60分，标签即为GOOD

s1=pd.DataFrame(SUM)
s1['BLOCK2']=SUM2
s1.columns=['SCORE','SCORE2']
# print(df.BLOCK)
# print(df.groupby('CLASS')['NUM'].count())
# print(df.groupby('CLASS')['NUM'].count())
# print(df.groupby('CLASS').count())

# fig, axes = plt.subplots(2, 2)  # fig, axes = plt.subplots(nrows, nclos, sharex, sharey)  #创建图像，指定行、列、共享x轴刻度、共享y轴刻度
# one = df.groupby('BLOCK')['BLOCK'].count()
# two = df.groupby('BLOCK2')['BLOCK2'].count()
# # # three=df.groupby('CLASS')['SCORE']
# one.plot(title='chengji1', kind='bar', color='red', ax=axes[0,0], legend=True, label='SCORE1', grid=True, alpha=0.5)#设置图像在0行0列
# two.plot(title='chengji2', kind='bar', color='blue', ax=axes[1,1], legend=True, label='SCORE2', grid=True, alpha=0.5)#设置图像在1行1列
# # three.plot(title='chengji',kind='line',color='red',legend=True,label='SCORE1',grid=True,alpha=0.5)
# plt.show()


# fig,axes = plt.subplots(2, 1)
# data = pd.Series(np.random.randn(16), index=list('abcdefghijklmnop'))
# data.plot(kind='bar', ax=axes[1], color='k', alpha=0.7)
# data.plot(kind='barh', ax=axes[0], color='k', alpha=0.7)
# plt.show()

# one = df.groupby('BLOCK')['BLOCK'].count()
# print(one)
# two = df.groupby('BLOCK2')['BLOCK2'].count()
# # three=df.groupby('CLASS')['SCORE']
# one.plot(title='chengji1', kind='bar', color='red',left=0.2,width=0.5, legend=True, label='SCORE1', grid=True, alpha=0.5)  # 设置图像在0行0列
# two.plot(title='chengji2', kind='bar', color='black',left=1,width=0.5, legend=True, label='SCORE2', grid=True, alpha=0.5)  # 设置图像在1行1列
# three.plot(title='chengji',kind='line',color='red',legend=True,label='SCORE1',grid=True,alpha=0.5)
fig,axes = plt.subplots(2, 1)
p=pd.DataFrame(s1,columns=['SCORE','SCORE2'],index=range(0,101,10))
p.plot(kind='bar',ax=axes[0],color=['yellow','red'],grid=True,alpha=0.7)
p.plot(kind='line',ax=axes[1],color=['green','blue'],grid=True,alpha=0.7)
plt.show()
e=df.groupby('BLOCK')['BLOCK'].count()
f=df.groupby('BLOCK2')['BLOCK2'].count()
print("请输入想要查询的分数段(输入exit退出)：")

while True:
    try:
        a = int(input())
        print("第一次成绩中,{}分的人总共有:{}人".format(a, e.ix[a]))
        print("第二次成绩中,{}分的人总共有:{}人".format(a, f.ix[a]))
    except:
        break

# df.to_excel("bb3.xlsx")
# print(df[df.SCORE2<df.SCORE+10][df.SCORE2>df.SCORE-10][df.SCORE>60][df.SCORE2>60])
# print(df[(df.SCORE>60)&(df.SCORE2>60)])
# print(df[(df.SCORE-df.SCORE2<=10)&(df.SCORE-df.SCORE2>=-10)&(df.SCORE>=60)&(df.SCORE2>=60)])#打印两次成绩相差10以内，并且都大于60分
# print(df[df.MAJOR.str.startswith('17')])#筛选出，专业为17开头的人
# print(df[df.CLASS.str.startswith('2017-1-1')])  # 筛选出行政班为一班的人

# print(df.iloc[0])#获取第0行数据

# df = df.set_index(['SCORE'])  # 设置索引，将SCORE设置为新的索引
# print(df[:1])#输出第一行数据，索引已变成姓名
# print(df.index)  # 这里也可以看出，索引全部变成了姓名

# print(df.sort_values('SCORE'))#按“SCORE”进行升序排序
# print(df.sort_index(ascending=False))  # 按照索引进行降序排序
# print(df.sort_index())  # 按照索引进行升序排序，
# print(df.sort_index(axis=1))#按第一列进行升序排序


# plt.xlabel('Age range')
# plt.ylabel('Number')
# plt.title('The statistics of face age dataset')
# a = plt.subplot(1, 1, 1)
#
# plt.ylim=(10, 40000)
# x = [10, 20, 30, 40, 50, 60, 70]
# x1 = [7, 17, 27, 37, 47, 57, 67]
# x2 = [13, 23, 33, 43, 53, 63, 73]
#
# Y1 = [41, 39, 13, 69, 39, 14, 7]
# Y2 = [0, 15, 20, 105, 79, 37, 43]
# Y3 = [0, 91, 404, 464, 521, 375, 553]
#
# #这里需要注意在画图的时候加上label在配合plt.legend（）函数就能直接得到图例，简单又方便！
#
# plt.bar(x1, Y1, facecolor='red', width=3, label = 'FG-NET')
# plt.bar(x, Y2, facecolor='green', width=3, label = 'MORPH')
# plt.bar(x2, Y3, facecolor='blue', width=3, label = 'CACD2000')
#
# plt.legend()
#
# plt.show()
