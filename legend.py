import matplotlib
from matplotlib.patches import Rectangle, Wedge
import matplotlib.pyplot as plt

# fix x:y ratio of plot
fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(111)

# draw outer and inner Wedge
outer=Wedge((0.4, .5), 0.5, 0, 30, color='g', alpha=0.5, transform=ax.transAxes)
inner=Wedge((0.4, .5), 0.3, 7.5, 22.5, color='g', alpha=0.6, transform=ax.transAxes)

ax.add_artist(outer)
ax.add_artist(inner)

# add text, change text background to transparent with bbox
ax.text(0.8, 0.6, "Normal", bbox=(dict(alpha=0)),
            ha='center', va='top', color='black', zorder=11, transform=ax.transAxes, fontsize=13)

ax.text(0.65, 0.58, "HD", bbox=(dict(alpha=0)),
            ha='center', va='top', color='black', zorder=11, transform=ax.transAxes, fontsize=12)

plt.show()