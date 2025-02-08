import matplotlib.pyplot as plt
import numpy as np

# Example data (replace with your actual data)
iterations = np.arange(10)  # X-axis: 0 to 9
log_loss_gradient = [0.9, 0.7, 0.55, 0.45, 0.35, 0.28, 0.22, 0.19, 0.16, 0.14]
log_loss_hessian = [0.8, 0.6, 0.5, 0.4, 0.32, 0.26, 0.2, 0.18, 0.15, 0.12]
log_loss_proposed = [0.7, 0.5, 0.4, 0.3, 0.25, 0.2, 0.18, 0.15, 0.12, 0.1]

# Dataset names, y-axis limits, and custom y-ticks
datasets = [
    ("ecoli-0-3-4_vs_5", (0.1, 1.0), np.round(np.linspace(0.1, 1.0, 10), 2)),  # Y-axis ticks: 0.1 to 1.0
    ("haberman", (0.52, 0.68), np.round(np.linspace(0.52, 0.68, 9), 2)),        # Y-axis ticks: 0.52 to 0.68
    ("glass0", (0.50, 0.66), np.round(np.linspace(0.50, 0.66, 9), 2)),          # Y-axis ticks: 0.50 to 0.66
    ("vowel0", (0.1, 1.0), np.round(np.linspace(0.1, 1.0, 10), 2)),             # Y-axis ticks: 0.1 to 1.0
    ("wisconsin", (0.25, 0.70), np.round(np.linspace(0.25, 0.70, 10), 2)),      # Y-axis ticks: 0.25 to 0.70
    ("segment0", (0.0, 1.0), [0.0, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9, 1.0]),    # Y-axis ticks: Custom list
]

# Create the subplots
fig, axes = plt.subplots(3, 2, figsize=(8, 10))
axes = axes.flatten()  # Flatten the 2D array of axes for easier iteration
fig.suptitle("Log-Loss vs Iterations", fontsize=14)

# Define line styles
line_styles = {
    "gradient": {"color": "red", "linestyle": ":", "label": "gradient", "linewidth": 2},
    "hessian": {"color": "blue", "linestyle": "--", "label": "Hessian", "linewidth": 2},
    "proposed": {"color": "green", "linestyle": "-", "label": "proposed", "linewidth": 2},
}

# Plot each dataset with corresponding y-axis limits and custom ticks
for i, (dataset, y_limits, y_ticks) in enumerate(datasets):
    ax = axes[i]
    ax.plot(iterations, log_loss_gradient, **line_styles["gradient"])
    ax.plot(iterations, log_loss_hessian, **line_styles["hessian"])
    ax.plot(iterations, log_loss_proposed, **line_styles["proposed"])
    
    ax.set_title(dataset, fontsize=10)
    ax.set_xlabel("Iterations", fontsize=9)
    ax.set_ylabel("Log-Loss", fontsize=9)
    ax.grid(True, linestyle=':', color='black', alpha=0.6)  # Matching grid style
    ax.legend(fontsize=8, loc="best")  # Legend settings

    # Set specific x-axis and y-axis limits and ticks for each plot
    ax.set_xlim(0, 9)  # X-axis: Iterations from 0 to 9
    ax.set_xticks(range(0, 10))  # Tick marks at 0, 1, 2, ..., 9
    ax.set_ylim(*y_limits)  # Y-axis: Based on specific limits
    ax.set_yticks(y_ticks)  # Custom y-ticks

# Adjust layout to ensure it matches the uploaded style
plt.subplots_adjust(hspace=0.4, wspace=0.3, top=0.9, bottom=0.05, left=0.1, right=0.95)
plt.show()