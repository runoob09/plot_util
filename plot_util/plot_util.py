from matplotlib import pyplot as plt
import numpy as np


def plot_performance(x, data, x_label, y_label, save_path=None):
    """
    绘制不同算法的性能表现
    :return:
    """
    cmap = plt.get_cmap("viridis")
    colors = [cmap(i*100) for i in range(len(data))]  # 获取的颜色数量
    plt.figure(figsize=(8, 6))
    for i, (key, value) in enumerate(data.items()):
        value_max = np.max(value,axis=0)
        value_min = np.min(value,axis=0)
        print(colors[i])
        plt.fill_between(x, value_min, value_max, color=colors[i], alpha=0.5)  # 绘制误差区间
        value_avg = np.average(value,axis=0)
        plt.plot(x, value_avg, color=colors[i], label=key)
    plt.legend()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    # 参数设置
    A = 0.1  # 振幅
    k = 0.5  # 频率
    noise_scale = 0.1  # 噪声幅度

    # 数据生成
    x = np.linspace(0, 20, 50)  # 平稳数据范围
    y_data1 = []
    for i in range(10):
        y = A * np.sin(k * x)  # 正弦函数
        noise = np.random.normal(0, noise_scale, size=x.shape)  # 小噪声
        y_noisy = y + noise
        y_data1.append(y_noisy)
    # 参数设置
    a = 0.5  # 线性斜率
    b = 1  # 截距
    noise_scale = 0.2  # 噪声幅度

    y_data2 = []
    for i in range(10):
        y = a * x + b  # 线性函数
        noise = np.random.normal(0, noise_scale, size=x.shape)  # 小噪声
        y_noisy = y + noise
        y_data2.append(y_noisy)
    data = {"PPO": np.array(y_data1), "DDPG": np.array(y_data2)}
    plot_performance(x, data, x_label="epoch", y_label="win rate", save_path=None)
