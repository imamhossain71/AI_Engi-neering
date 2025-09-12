import matplotlib.pyplot as plt
import numpy as np

# # Sample data
# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)

# # Create figure with custom size and resolution
# plt.figure(figsize=(10, 6), dpi=100, facecolor="lightyellow")

# # Plot sine curve
# plt.plot(x, y1, label="Sine", color="blue", linewidth=2, linestyle="--")

# # Plot cosine curve
# plt.plot(x, y2, label="Cosine", color="red", linewidth=2)

# # Add title with font customization
# plt.title("Sine and Cosine Functions", fontsize=16, fontweight="bold", color="darkgreen")

# # Add labels
# plt.xlabel("X axis →", fontsize=12)
# plt.ylabel("Y axis →", fontsize=12)

# # Add legend with custom location
# plt.legend(loc="upper right", fontsize=12, shadow=True)

# # Add gridlines
# plt.grid(True, linestyle=":", color="gray", alpha=0.7)

# # Add annotation (arrow pointing)
# plt.annotate("Peak of sine", xy=(np.pi/2, 1), xytext=(2, 1.3),
#              arrowprops=dict(facecolor="black", shrink=0.05))

# # Show plot
# plt.show()


x2 = np.linspace(0, 20, 200)
y3 = np.sin(x2) * np.exp(-0.1*x2)   # Damped Sine Wave
y4 = np.cos(x2) * np.exp(-0.1*x2)   # Damped Cosine Wave

plt.figure(figsize=(12, 6), dpi=100, facecolor="whitesmoke")
plt.plot(x2, y3, label="Damped Sine", color="green", linewidth=2, linestyle=":")
plt.plot(x2, y4, label="Damped Cosine", color="purple", linewidth=2)
plt.title("Damped Sine & Cosine Waves", fontsize=16, fontweight="bold", color="navy")
plt.xlabel("X axis →", fontsize=12)
plt.ylabel("Y axis →", fontsize=12)
plt.legend(loc="lower center", fontsize=12, shadow=True)
plt.grid(True, linestyle="--", color="red", alpha=0.5)
plt.annotate("First Cosine Peak", 
             xy=(0, 1), xytext=(3, 1.2),   # Peak at (0,1)
             arrowprops=dict(facecolor="black", arrowstyle="->"))
plt.show()




