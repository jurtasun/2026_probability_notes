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
# Linear, Quadratic, Sinusoidal examples
# =========================

x = np.linspace(-5, 5, 1000)

# -------- Linear --------
f_linear = lambda x: x

fig, ax = plt.subplots(figsize=figsize)
ax.plot(x, f_linear(x), color='black', lw=1.7, alpha=0.3)

# Axes styling
for spine in ax.spines.values():
    spine.set_visible(False)

ax.annotate("", xy=(5.5, 0), xytext=(-5.5, 0),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax.annotate("", xy=(0, 5.5), xytext=(0, -5.5),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

ax.set_xlim(-5.5, 5.5)
ax.set_ylim(-5.5, 5.5)

ax.text(5.4, -0.3, r"$x$", fontsize=14, ha='right')
ax.text(0.2, 5.4, r"$y(x)$", fontsize=14, va='bottom')

ax.tick_params(axis='both', direction='in', length=4, width=1)
ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
fig.savefig("linear.png", dpi=300, bbox_inches='tight')
fig.savefig("linear.pdf", bbox_inches='tight')
plt.show()


# -------- Quadratic --------
f_quad = lambda x: x**2

fig, ax = plt.subplots(figsize=figsize)
ax.plot(x, f_quad(x), color='black', lw=1.7, alpha=0.3)

for spine in ax.spines.values():
    spine.set_visible(False)

ax.annotate("", xy=(5.5, 0), xytext=(-5.5, 0),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax.annotate("", xy=(0, 30), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

ax.set_xlim(-5.5, 5.5)
ax.set_ylim(-1, 30)

ax.text(5.4, -1, r"$x$", fontsize=14, ha='right')
ax.text(0.2, 29, r"$y(x)$", fontsize=14, va='bottom')

ax.tick_params(axis='both', direction='in', length=4, width=1)
ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
fig.savefig("quadratic.png", dpi=300, bbox_inches='tight')
fig.savefig("quadratic.pdf", bbox_inches='tight')
plt.show()


# -------- Sinusoidal --------
f_sin = lambda x: np.cos(x)

fig, ax = plt.subplots(figsize=figsize)
ax.plot(x, f_sin(x), color='black', lw=1.7, alpha=0.3)

for spine in ax.spines.values():
    spine.set_visible(False)

ax.annotate("", xy=(5.5, 0), xytext=(-5.5, 0),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax.annotate("", xy=(0, 1.5), xytext=(0, -1.5),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

ax.set_xlim(-5.5, 5.5)
ax.set_ylim(-1.5, 1.5)

ax.text(5.4, -0.2, r"$x$", fontsize=14, ha='right')
ax.text(0.2, 1.4, r"$y(x)$", fontsize=14, va='bottom')

ax.tick_params(axis='both', direction='in', length=4, width=1)
ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
fig.savefig("sinusoidal.png", dpi=300, bbox_inches='tight')
fig.savefig("sinusoidal.pdf", bbox_inches='tight')
plt.show()