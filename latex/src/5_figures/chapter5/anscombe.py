# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, norm, uniform, expon



# Plot styling
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Palatino", "Computer Modern Roman"],
    "mathtext.fontset": "cm",
    "axes.facecolor": "none",
    "figure.facecolor": "white",
})

# Colors
main_color = "#1f77b4"
highlight_color = 'firebrick'
figsize = (7, 4.5)


# =========================
# -------- Anscombe Quartet --------
# =========================

# Anscombe data
x1 = np.array([10,8,13,9,11,14,6,4,12,7,5])
y1 = np.array([8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68])

x2 = x1
y2 = np.array([9.14,8.14,8.74,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74])

x3 = x1
y3 = np.array([7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73])

x4 = np.array([8,8,8,8,8,8,8,19,8,8,8])
y4 = np.array([6.58,5.76,7.71,8.84,8.47,7.04,5.25,12.50,5.56,7.91,6.89])

datasets = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]

fig, axes = plt.subplots(2, 2, figsize=(8, 7))

for ax, (x_d, y_d) in zip(axes.flatten(), datasets):

    # Scatter points
    ax.scatter(x_d, y_d, color=highlight_color, s=20, alpha=0.7)

    # Regression line (same slope/intercept)
    slope, intercept = np.polyfit(x_d, y_d, 1)
    x_line = np.linspace(2, 20, 100)
    ax.plot(x_line, slope*x_line + intercept,
            color='black', lw=1.5, alpha=0.5)

    # Style: remove spines
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Axes arrows
    ax.annotate("", xy=(20.5, 3), xytext=(2, 3),
                arrowprops=dict(arrowstyle="->", lw=1.2, color='black'))
    ax.annotate("", xy=(2, 14), xytext=(2, 3),
                arrowprops=dict(arrowstyle="->", lw=1.2, color='black'))

    # Limits
    ax.set_xlim(2, 20)
    ax.set_ylim(3, 14)

    # Labels (only outer for cleanliness)
    ax.tick_params(axis='both', direction='in', length=3, width=1)
    ax.grid(True, linestyle='--', alpha=0.3)

# Global labels
fig.text(0.5, 0.04, r"$x$", ha='center', fontsize=14)
fig.text(0.04, 0.5, r"$y(x)$", va='center', rotation='vertical', fontsize=14)

plt.tight_layout(rect=[0.05, 0.05, 1, 1])

fig.savefig("anscombe.png", dpi=300, bbox_inches='tight')
fig.savefig("anscombe.pdf", bbox_inches='tight')

plt.show()