import numpy as np
import matplotlib.pyplot as plt


plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],})
CL = {
    'ORA': '#EE7733',  # orange 橙
    'BLU': '#0077BB',  # blue 蓝
    'CYA': '#33BBEE',  # cyan 青
    'MAG': '#EE3377',  # magenta 品红
    'RED': '#CC3311',  # red 红
    'TEA': '#009988',  # teal 蓝绿
    'GRE': '#BBBBBB',  # grey 灰色
}


""" Import """
sample_data = np.genfromtxt("Engine Temperature Sensor.csv", delimiter=",")
N = np.arange(sample_data.shape[0])


""" Process """
sigma_0 = 10
mu_0 = 100
k = 3

UCL = mu_0 + sigma_0 * k
LCL = mu_0 - sigma_0 * k


""" Plot """
# * Shewhart control chart
# fig, ax = plt.subplots(figsize=(8, 6), dpi=200)
# ax.hlines([UCL, LCL], N[0] - 10, N[-1] + 10, colors=CL['RED'], linestyles='dotted', label='UCL \& LCL', lw=3)
# ax.hlines([mu_0], N[0] - 10, N[-1] + 10, colors=CL['MAG'], linestyles='dashed', label='CL', lw=4)
# ax.plot(N, sample_data, '.-', c=CL['BLU'], label='data', lw=3, ms=8, mew=6)
# # ax.axis('equal')
# ax.set_xlim([0, N[-1]])
# # ax.set_ylim([-100, 100])
# # ax.xaxis.set_ticks([])
# # ax.yaxis.set_ticks([])
# ax.set_xlabel('samples', fontsize=20)
# ax.set_ylabel('values (deg)', fontsize=20)
# # plt.pause(0.01)  # 暂停
# ax.legend(loc='lower right', fontsize=12)  # 标签位置
# ax.grid(linestyle='--')
# plt.tight_layout()
# plt.savefig("figure/Shewhart control chart result.jpg")



plt.show()