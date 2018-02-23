import pandas as pd
import numpy as np

print("请输入想要打开的文件：")
name = input()
try:
    df = pd.read_excel(name)
    print("打开成功！")
except:
    print("无此文件！")
    exit(1)
print("列名为：", df.columns)
while True:
    try:


# print("输入序号，选择功能：")
# print("1.\t查看数据概括")
