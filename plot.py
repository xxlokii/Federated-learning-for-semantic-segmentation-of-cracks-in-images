# plot the log
import matplotlib.pyplot as plt
import numpy as np
AsphaltCrack_mIOU_0d1_0 = [0.49, 0.18, 0.49, 0.45, 0.25, 0.37, 0.49, 0.5, 0.54,
                           0.52, 0.5, 0.47, 0.55, 0.56, 0.51, 0.51, 0.5, 0.53, 0.53, 0.51]
AsphaltCrack_mIOU_0d5_0 = [0.49, 0.49, 0.26, 0.46, 0.4, 0.4, 0.5, 0.51, 0.52,
                           0.52, 0.55, 0.56, 0.56, 0.56, 0.57, 0.58, 0.58, 0.58, 0.58, 0.57]
AsphaltCrack_mIOU_1_0 = [0.49, 0.49, 0.48, 0.39, 0.48, 0.43, 0.5, 0.5, 0.53,
                         0.54, 0.56, 0.57, 0.57, 0.57, 0.58, 0.58, 0.58, 0.58, 0.59, 0.59]
AsphaltCrack_mIOU_0d1_1 = [0.49, 0.49, 0.49, 0.48, 0.51, 0.49, 0.47, 0.52,
                           0.53, 0.53, 0.47, 0.52, 0.48, 0.57, 0.53, 0.58, 0.58, 0.58, 0.59, 0.44]
AsphaltCrack_mIOU_0d5_1 = [0.49, 0.49, 0.49, 0.5, 0.52, 0.53, 0.52, 0.54,
                           0.54, 0.56, 0.56, 0.57, 0.57, 0.58, 0.6, 0.59, 0.58, 0.58, 0.61, 0.6]
AsphaltCrack_mIOU_1_1 = [0.49, 0.49, 0.49, 0.49, 0.51, 0.53, 0.53, 0.53,
                         0.55, 0.56, 0.57, 0.58, 0.57, 0.6, 0.59, 0.6, 0.59, 0.59, 0.6, 0.6]
ConcreteCrack_mIOU_0d1_0 = [0.11, 0.49, 0.57, 0.8, 0.77, 0.59, 0.82, 0.79,
                            0.8, 0.83, 0.73, 0.85, 0.84, 0.85, 0.83, 0.84, 0.85, 0.85, 0.86, 0.6]
ConcreteCrack_mIOU_0d5_0 = [0.49, 0.49, 0.6, 0.79, 0.84, 0.85, 0.86, 0.85,
                            0.86, 0.84, 0.86, 0.86, 0.86, 0.86, 0.86, 0.86, 0.86, 0.87, 0.87, 0.86]
ConcreteCrack_mIOU_1_0 = [0.49, 0.49, 0.56, 0.76, 0.83, 0.85, 0.86, 0.86,
                          0.86, 0.86, 0.86, 0.86, 0.86, 0.86, 0.87, 0.87, 0.87, 0.87, 0.87, 0.87]
ConcreteCrack_mIOU_0d1_1 = [0.02, 0.49, 0.5, 0.79, 0.81, 0.83, 0.84, 0.84,
                            0.85, 0.85, 0.84, 0.84, 0.85, 0.85, 0.85, 0.85, 0.85, 0.86, 0.86, 0.86]
ConcreteCrack_mIOU_0d5_1 = [0.49, 0.49, 0.59, 0.8, 0.84, 0.85, 0.85, 0.85,
                            0.86, 0.86, 0.86, 0.86, 0.86, 0.85, 0.86, 0.87, 0.87, 0.87, 0.87, 0.87]
ConcreteCrack_mIOU_1_1 = [0.49, 0.49, 0.53, 0.61, 0.83, 0.85, 0.85, 0.85,
                          0.86, 0.86, 0.86, 0.86, 0.86, 0.86, 0.86, 0.87, 0.87, 0.86, 0.87, 0.87]
AsphaltCrack_0d1_0 = np.array(AsphaltCrack_mIOU_0d1_0)
AsphaltCrack_0d5_0 = np.array(AsphaltCrack_mIOU_0d5_0)
AsphaltCrack_1_0 = np.array(AsphaltCrack_mIOU_1_0)

AsphaltCrack_0d1_1 = np.array(AsphaltCrack_mIOU_0d1_1)
AsphaltCrack_0d5_1 = np.array(AsphaltCrack_mIOU_0d5_1)
AsphaltCrack_1_1 = np.array(AsphaltCrack_mIOU_1_1)

ConcreteCrack_0d1_0 = np.array(ConcreteCrack_mIOU_0d1_0)
ConcreteCrack_0d5_0 = np.array(ConcreteCrack_mIOU_0d5_0)
ConcreteCrack_1_0 = np.array(ConcreteCrack_mIOU_1_0)

ConcreteCrack_0d1_1 = np.array(ConcreteCrack_mIOU_0d1_1)
ConcreteCrack_0d5_1 = np.array(ConcreteCrack_mIOU_0d5_1)
ConcreteCrack_1_1 = np.array(ConcreteCrack_mIOU_1_1)

# create a figure with 4 subplots, arranged in a 2x2 grid
fig, axs = plt.subplots(2, 2, figsize=(10, 5))

# first plot
# title is non-iid distribution
axs[0, 0].set_title('Non-iid distribution')
# x axis is number of communication rounds, but only show 1, 5, 10, 15, 20
axs[0, 0].set_xticks(np.arange(0, 20, 1))
# x label is number of communication rounds
axs[0, 0].set_xlabel('Communication rounds')
# y label is mIOU
axs[0, 0].set_ylabel('mIOU')
# plot the mIOU of different models
axs[0, 0].plot(AsphaltCrack_0d1_0, label='0.1')
axs[0, 0].plot(AsphaltCrack_0d5_0, label='0.5')
axs[0, 0].plot(AsphaltCrack_1_0, label='1.0')
axs[0, 0].legend(title='Client fraction', loc='lower right')

# second plot
# title is iid distribution
axs[0, 1].set_title('iid distribution')
# x axis is number of communication rounds
axs[0, 1].set_xticks(np.arange(0, 20, 1))
# x label is number of communication rounds
axs[0, 1].set_xlabel('Communication rounds')
# y label is mIOU
axs[0, 1].set_ylabel('mIOU')
# plot the mIOU of different models
axs[0, 1].plot(AsphaltCrack_0d1_1, label='0.1')
axs[0, 1].plot(AsphaltCrack_0d5_1, label='0.5')
axs[0, 1].plot(AsphaltCrack_1_1, label='1.0')
# the legend title is client fraction and the legend is shown in the down right corner
axs[0, 1].legend(title='Client fraction', loc='lower right')

# third plot
# title is non-iid distribution
axs[1, 0].set_title('Non-iid distribution')
# x axis is number of communication rounds
axs[1, 0].set_xticks(np.arange(0, 20, 1))
# x label is number of communication rounds
axs[1, 0].set_xlabel('Communication rounds')
# y label is mIOU
axs[1, 0].set_ylabel('mIOU')
# plot the mIOU of different models
axs[1, 0].plot(ConcreteCrack_0d1_0, label='0.1')
axs[1, 0].plot(ConcreteCrack_0d5_0, label='0.5')
axs[1, 0].plot(ConcreteCrack_1_0, label='1.0')
axs[1, 0].legend(title='Client fraction', loc='lower right')

# fourth plot
# title is iid distribution
axs[1, 1].set_title('iid distribution')
# x axis is number of communication rounds
axs[1, 1].set_xticks(np.arange(0, 20, 1))
# x label is number of communication rounds
axs[1, 1].set_xlabel('Communication rounds')
# y label is mIOU
axs[1, 1].set_ylabel('mIOU')
# plot the mIOU of different models
axs[1, 1].plot(ConcreteCrack_0d1_1, label='0.1')
axs[1, 1].plot(ConcreteCrack_0d5_1, label='0.5')
axs[1, 1].plot(ConcreteCrack_1_1, label='1.0')
axs[1, 1].legend(title='Client fraction', loc='lower right')

# set title for the first two subplots
axs[0, 0].set_title('AsphaltCrack Non-iid')
axs[0, 1].set_title('AsphaltCrack iid')
axs[1, 0].set_title('ConcreteCrack Non-iid')
axs[1, 1].set_title('ConcreteCrack iid')

# adjust the space between subplots
fig.tight_layout(pad=1.0)

# save the figure
plt.savefig('mIOU.png')
