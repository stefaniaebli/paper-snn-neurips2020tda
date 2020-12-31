#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def main():
    total_notsee=[10,20,30,40,50]
    total_notsee_x=[0,10,20,30,40,50]

    plt.rcParams.update({"font.size": 6})

    fig = plt.figure(figsize=(80/25.4, 35/25.4))

    gs = fig.add_gridspec(1, 3, hspace=0.0)
    axs = gs.subplots(sharey="row")

    for d in [0, 1, 2]:
        m = np.load("transferlearning_m_mean_dim{}.npy".format(d), allow_pickle=False)
        h = np.load("transferlearning_h_std_dim{}.npy".format(d), allow_pickle=False)


        axs[d].set_title("Dimension %d" %(d))
        axs[d].plot(total_notsee, m, c="C%d" %(d))
        axs[d].fill_between(total_notsee, m-h, m+h, alpha=.2, zorder=0, color="C%d" %(d))
        axs[d].set_xlim((10, 50))
        axs[d].set_ylim((55,95))
        axs[d].set_xticks([10, 20, 30, 40,50])
        axs[d].set_yticks([60, 70, 80, 90])

    
    axs[0].set_ylabel("Accuracy")
    axs[1].set_xlabel("% missing")

    fig.tight_layout()
    fig.savefig("foo-transfer.pdf")
        

if __name__ == "__main__":
    main()
