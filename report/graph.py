import numpy as np
import matplotlib.pyplot as plt

# Parameters
d0 = 1.5  # choose any positive value
mu0 = 0.0
mu1 = d0**2
sigma = d0

# Grid in G
G = np.linspace(mu0 - 4*sigma, mu1 + 4*sigma, 1000)

# PDFs
P0 = 1.0 / (np.sqrt(2*np.pi) * sigma) * np.exp(-(G - mu0)**2 / (2 * sigma**2))
P1 = 1.0 / (np.sqrt(2*np.pi) * sigma) * np.exp(-(G - mu1)**2 / (2 * sigma**2))

fig, ax = plt.subplots(figsize=(7, 4))

# Plot both curves as black solid lines
ax.plot(G, P0, color='black')
ax.plot(G, P1, color='black')

# Remove ticks and frame
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

# Baseline
ax.axhline(0, color='black', linewidth=0.8)

# Heights
y0 = P0.max()
y1 = P1.max()
ymax = max(y0, y1)

# Label each curve near its peak
ax.text(mu0, y0*0.9, r'$P_0(G)$', ha='center', va='bottom')
ax.text(mu1, y1*0.9, r'$P_1(G)$', ha='center', va='bottom')

# Vertical lines at means
ax.axvline(mu0, color='black', linestyle=':', alpha=0.7)
ax.axvline(mu1, color='black', linestyle=':', alpha=0.7)

# Label the means
ax.text(mu0, -ymax*0.08, r'$0$', ha='center', va='top')
ax.text(mu1, -ymax*0.08, r'$d_0^2$', ha='center', va='top')


# Floating label for G-axis
ax.text(G.mean(), -ymax*0.18, r'$G$', ha='center', va='center')

plt.tight_layout()
plt.show()
