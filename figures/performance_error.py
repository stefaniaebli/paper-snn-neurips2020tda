#!/usr/bin/env python3

import os
import numpy as np
import matplotlib.pyplot as plt


def main():

    plt.rcParams.update({"font.size": 6})

    fig = plt.figure(constrained_layout=True, figsize=(80/25.4, 35/25.4))

    gs = fig.add_gridspec(1, 3)
    axs = gs.subplots()

    for d in [0, 1, 2]:
        errors = np.load("data/error_dim%d_notsee40.npy" %(d), allow_pickle=False)

        (hist, edges) = np.histogram(np.log10(errors), bins=50)

        axs[d].set_title("Dimension %d" %(d))
        axs[d].bar(edges[0:-1], hist, width=edges[1:] - edges[0:-1], color="C%d" %(d))

        axs[d].set_xscale("log")
        axs[d].set_xticks([1e-2, 1e-1, 1e0])
        # axs[d].get_xaxis().get_major_formatter().labelOnlyBase = False

    axs[0].set_ylabel("Count")
    axs[1].set_xlabel("Error")

    fig.tight_layout()
    filename = os.path.splitext(os.path.basename(__file__))[0] + '.pdf'
    fig.savefig(filename)


if __name__ == "__main__":
    main()
