# import matplotlib.pyplot as plt
# import numpy as np

# # Data
# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# y3 = np.exp(-0.1 * x) * np.sin(x)
# y4 = x**2

# # Subplots → 2x2 Grid
# fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# axs[0,0].plot(x, y1, color="blue")
# axs[0,0].set_title("Sine Wave")

# axs[0,1].plot(x, y2, color="red")
# axs[0,1].set_title("Cosine Wave")

# axs[1,0].plot(x, y3, color="green")
# axs[1,0].set_title("Damped Sine")

# axs[1,1].plot(x, y4, color="purple")
# axs[1,1].set_title("Quadratic Function")

# plt.tight_layout()
# plt.show()

# # Multiple Figures
# plt.figure(1)
# plt.plot(x, y1, label="Sine")
# plt.legend()

# plt.figure(2)
# plt.plot(x, y2, label="Cosine", color="orange")
# plt.legend()

# plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)

# Functions
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x**2
y4 = np.exp(-0.1 * x) * np.cos(x)

# Subplots (2x2 Grid)
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

axs[0,0].plot(x, y1, color="blue")
axs[0,0].set_title("Sine Wave")
axs[0,0].grid(True)

axs[0,1].plot(x, y2, color="red")
axs[0,1].set_title("Cosine Wave")
axs[0,1].grid(True)

axs[1,0].plot(x, y3, color="green")
axs[1,0].set_title("Quadratic Function")
axs[1,0].grid(True)

axs[1,1].plot(x, y4, color="purple")
axs[1,1].set_title("Damped Cosine")
axs[1,1].grid(True)

plt.tight_layout()
plt.show()

# Multiple Figures
plt.figure(1)
plt.plot(x, y1, label="Sine", color="blue")
plt.legend()

plt.figure(2)
plt.plot(x, y2, label="Cosine", color="red")
plt.legend()

plt.show()

