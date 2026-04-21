# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Plot styling
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Palatino", "Computer Modern Roman"],
    "mathtext.fontset": "cm",
    "axes.facecolor": "none",
    "figure.facecolor": "white",
})

# Colors and size
highlight_color = 'firebrick'
figsize = (7, 4.5)

# Domain
x = np.linspace(-5, 5, 1000)


# =========================
# -------- Linear --------
# =========================
f_linear = lambda x: x
noise = 0.8

fig, ax = plt.subplots(figsize=figsize)
ax.plot(x, f_linear(x), color='black', lw=1.7, alpha=0.6)

# Noise band
ax.fill_between(x, f_linear(x)-noise, f_linear(x)+noise,
                color=highlight_color, alpha=0.1)

# Sample noisy points
x_sample = np.linspace(-4, 4, 20)
y_sample = f_linear(x_sample) + np.random.normal(0, noise, size=len(x_sample))
ax.scatter(x_sample, y_sample, color=highlight_color, s=15, alpha=0.6)

# Axes
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
fig.savefig("linear_noise.png", dpi=300, bbox_inches='tight')
fig.savefig("linear_noise.pdf", bbox_inches='tight')
plt.show()


# =========================
# -------- Quadratic --------
# =========================
f_quad = lambda x: x**2
noise = 2.5

fig, ax = plt.subplots(figsize=figsize)
ax.plot(x, f_quad(x), color='black', lw=1.7, alpha=0.6)

ax.fill_between(x, f_quad(x)-noise, f_quad(x)+noise,
                color=highlight_color, alpha=0.1)

x_sample = np.linspace(-4, 4, 20)
y_sample = f_quad(x_sample) + np.random.normal(0, noise, size=len(x_sample))
ax.scatter(x_sample, y_sample, color=highlight_color, s=15, alpha=0.6)

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
fig.savefig("quadratic_noise.png", dpi=300, bbox_inches='tight')
fig.savefig("quadratic_noise.pdf", bbox_inches='tight')
plt.show()


# =========================
# -------- Sinusoidal --------
# =========================
f_sin = lambda x: np.cos(x)
noise = 0.4

fig, ax = plt.subplots(figsize=figsize)
ax.plot(x, f_sin(x), color='black', lw=1.7, alpha=0.6)

ax.fill_between(x, f_sin(x)-noise, f_sin(x)+noise,
                color=highlight_color, alpha=0.1)

x_sample = np.linspace(-4, 4, 20)
y_sample = f_sin(x_sample) + np.random.normal(0, noise, size=len(x_sample))
ax.scatter(x_sample, y_sample, color=highlight_color, s=15, alpha=0.6)

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
fig.savefig("sinusoidal_noise.png", dpi=300, bbox_inches='tight')
fig.savefig("sinusoidal_noise.pdf", bbox_inches='tight')
plt.show()