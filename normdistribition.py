import numpy as np  
import matplotlib.pyplot as plt  
from scipy.stats import norm  
  
# 定义正态分布的均值和标准差  
mu = 0  # 均值  
sigma = 1  # 标准差  
  
# 生成正态分布的数据点  
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)  
  
# 计算正态分布的概率密度函数（PDF）  
y = norm.pdf(x, mu, sigma)  
  
# 绘制曲线  
plt.plot(x, y, 'r-', lw=5, alpha=0.6, label='normal pdf')  
  
# 设置图表的标题和坐标轴标签  
plt.title("正态分布曲线")  
plt.xlabel("值")  
plt.ylabel("概率密度")  
  
# 设置图例  
plt.legend(loc='best')  
  
# 显示网格  
plt.grid(True)  
  
# 显示图表  
plt.show()
