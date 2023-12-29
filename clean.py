import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
import numpy as np

file_path = "./data/2021finance.csv"
df = pd.read_csv(file_path, header=None)
#打印 DataFrame 的简短摘要
print(df.info())
#写入列名
df.columns = ['地区',
              '2020执行数',
              '2020执行数(剔除特殊转移支付)',
              '2021预算数']
#打印前几行列表，查看列表是否异常
df.head()

"""--------------画图-------------------"""
# 绘制折线图
def linePlot():
    plt.rcParams['font.family'] = 'Microsoft YaHei'
    plt.figure(figsize=(20, 8))
    plt.xticks(rotation=90)
    plt.xlabel("地区")
    plt.ylabel("人民币（亿元）")
    plt.title("2021年中央对地方一般公共预算转移支付分地区情况")
    plt.grid(True, linestyle='--', alpha=0.7)

    # 绘制图像
    for col in ['2020执行数', '2020执行数(剔除特殊转移支付)', '2021预算数']:
        plt.plot(df['地区'], df[col], label=col)

    plt.legend()
    plt.savefig('lineChart.png', dpi=400, bbox_inches='tight')
    plt.show()

# 绘制条形图
def barPlot():
    plt.rcParams['font.family'] = 'Microsoft YaHei'
    plt.figure(figsize=(20, 16), facecolor='white')
    plt.xlabel("人民币 单位（亿元）", fontsize=14)
    plt.ylabel("地区", fontsize=14)
    plt.title("2021年中央对地方一般公共预算转移支付分地区情况汇总表", fontsize=16)

    colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#9370DB']  # 例如：红色，蓝色，绿色，金色，紫色

    # 绘制水平条形图
    bars = plt.barh(df['地区'], df['2021预算数'], height=0.5, color=colors)

    # 添加数据标签
    for bar in bars:
        plt.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height() / 2, f'{bar.get_width():.2f}',
                 va='center', fontsize=14, color='black')

    plt.tight_layout()
    plt.savefig('2021barChart.png', dpi=400, bbox_inches='tight')
    plt.show()
