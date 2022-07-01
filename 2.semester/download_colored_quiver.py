import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def flow_legend():
    """
    show quiver plot to indicate how arrows are colored in the flow() method.
    https://stackoverflow.com/questions/40026718/different-colours-for-arrows-in-quiver-plot
    """
    ph = np.linspace(0, 2*np.pi, 13)
    x = np.cos(ph)
    y = np.sin(ph)
    u = np.cos(ph)
    v = np.sin(ph)
    colors = np.arctan2(u, v)

    norm = plt.Normalize()
    norm.autoscale(colors)
    # we need to normalize our colors array to match it colormap domain
    # which is [0, 1]

    colormap = cm.jet

    plt.figure(figsize=(6, 6))
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.quiver(x, y, u, v, color=colormap(norm(colors)),  angles='xy', scale_units='xy', scale=1)
    plt.show()

flow_legend()
