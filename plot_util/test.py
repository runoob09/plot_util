from matplotlib import pyplot as plt

cmap = plt.get_cmap("viridis")
colors = [cmap(i) for i in range(10)] # 获取的颜色数量
print(colors)