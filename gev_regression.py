import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate synthetic datasets for demonstration (replace with actual datasets)
datasets = {
    "ecoli": np.random.rand(10, 2),
    "haberman": np.random.rand(10, 2),
    "glass0": np.random.rand(10, 2),
    "vowel0": np.random.rand(10, 2),
    "wisconsin": np.random.rand(10, 2),
    "segment0": np.random.rand(10, 2),
}

# Log-loss data for the plots (gradient, Hessian, proposed methods)
log_loss_data = {
    "gradient": [np.exp(-0.5 * i) + 0.02 * np.random.rand() for i in range(10)],
    "hessian": [np.exp(-0.6 * i) + 0.02 * np.random.rand() for i in range(10)],
    "proposed": [np.exp(-0.8 * i) + 0.01 * np.random.rand() for i in range(10)],
}

# Table data (Brier scores for each method and dataset)
table_data = {
    "dataset": ["ecoli", "haberman", "glass0", "vowel0", "wisconsin", "segment0"],
    "GEV Regression": np.random.rand(6) / 10,
    "LOGIT": np.random.rand(6) / 10,
    "PROBIT": np.random.rand(6) / 10,
    "CLOGLOG": np.random.rand(6) / 10,
}

# Convert table data to DataFrame
table_df = pd.DataFrame(table_data)

# Plot log-loss graphs for each dataset
fig, axes = plt.subplots(3, 2, figsize=(10, 10))
fig.suptitle("Log-Loss vs Iterations", fontsize=16)

datasets_list = list(datasets.keys())

for i, ax in enumerate(axes.flatten()):
    if i >= len(datasets_list):
        ax.axis("off")
        continue

    dataset_name = datasets_list[i]
    ax.plot(range(10), log_loss_data["gradient"], "r--", label="gradient")
    ax.plot(range(10), log_loss_data["hessian"], "b--", label="hessian")
    ax.plot(range(10), log_loss_data["proposed"], "g-", label="proposed")

    ax.set_title(dataset_name, fontsize=10)
    ax.set_xlabel("Iterations")
    ax.set_ylabel("Log-Loss")
    ax.legend()

plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the graph
plt.savefig("log_loss_graphs.png")
plt.show()

# Save table as CSV
table_df.to_csv("brier_scores.csv", index=False)

# Print sample of the dataset (for viewing)
for name, data in datasets.items():
    print(f"Sample data from {name} dataset:")
    print(data[:5])  # Show the first 5 rows
    print()

# Print the table
print("Brier Scores Table:")
print(table_df)
