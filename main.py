import numpy as np
import matplotlib.pyplot as plt
# DONE delete idle lines
# DONE finish CUSUM part


plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],})
CL = {
    'BLU': '#0077BB',  # blue 蓝
    'CYA': '#33BBEE',  # cyan 青
    'MAG': '#EE3377',  # magenta 品红
    'RED': '#CC3311',  # red 红
}


""" Import """
sample_data = np.genfromtxt("Engine Temperature Sensor.csv", delimiter=",")
N = np.arange(sample_data.shape[0])


""" Process """
# Shewhart part
sigma_0 = 10
mu_0 = 100
k = 3

UCL = mu_0 + sigma_0 * k
LCL = mu_0 - sigma_0 * k

# CUSUM part
mu_1 = 110  # 10 deg of mean shift is not tolerated
K = np.fabs(mu_1 - mu_0) / 2
H = 5 * sigma_0

C_positive = [0]
C_negative = [0]

for i in range(N.shape[0]):
    C_positive_new = np.max([0, sample_data[i] - (mu_0 + K) + C_positive[i]])
    C_positive.append(C_positive_new)
    C_negative_new = np.max([0, (mu_0 - K) - sample_data[i] + C_negative[i]])
    C_negative.append(C_negative_new)
C_positive = np.asarray(C_positive)
C_negative = np.asarray(C_negative)


""" Plot """
# * Shewhart control chart
# fig, ax = plt.subplots(figsize=(8, 6), dpi=200)
# ax.hlines([UCL, LCL], N[0] - 10, N[-1] + 10, colors=CL['RED'], linestyles='dotted', label='UCL \& LCL', lw=3)
# ax.hlines([mu_0], N[0] - 10, N[-1] + 10, colors=CL['MAG'], linestyles='dashed', label='CL', lw=4)
# ax.plot(N, sample_data, '.-', c=CL['BLU'], label='data', lw=3, ms=8, mew=6)
# ax.set_xlim([0, N[-1]])
# ax.set_xlabel('samples', fontsize=20)
# ax.set_ylabel('values (deg)', fontsize=20)
# ax.legend(loc='lower right', fontsize=12)  # legend position
# ax.grid(linestyle='--')
# plt.tight_layout()
# # plt.savefig("figure/Shewhart control chart result.jpg")

# * CUSUM control chart
fig, ax = plt.subplots(figsize=(8, 6), dpi=200)
ax.hlines([H, - H], N[0] - 10, N[-1] + 10, colors=CL['RED'], linestyles='dotted', label='UCL \& LCL', lw=3)
ax.hlines([0], N[0] - 10, N[-1] + 10, colors=CL['MAG'], linestyles='dashed', label='CL', lw=4)
ax.plot(N, C_positive[1:], '.-', c=CL['BLU'], label='$C^+$', lw=3, ms=8, mew=6)
ax.plot(N, - C_negative[1:], '.-', c=CL['CYA'], label='$C^-$', lw=3, ms=8, mew=6)
ax.set_xlim([0, N[-1]])
ax.set_xlabel('samples', fontsize=20)
ax.set_ylabel('CUSUM values (deg)', fontsize=20)
ax.legend(loc='lower right', fontsize=12)  # legend position
ax.grid(linestyle='--')
plt.tight_layout()
# plt.savefig("figure/CUSUM control chart result.jpg")

plt.show()