# Define datasets
datasets = [
    "wisconsin", "glass0", "haberman", "segment0", "ecoli0345", "vowel0"
]

# Define model configurations
models = [
    "GEV REGRESSION", "LOGIT", "PROBIT", "CLOGLOG",
    "SMOTE + LOGIT", "SMOTE + PROBIT", "SMOTE + CLOGLOG"
]

# Example metric values
brier_scores = {
    "wisconsin": [0.02079, 0.02303, 0.02348, 0.03024, 0.02700, 0.02336, 0.03024],
    "glass0": [0.16470, 0.17362, 0.17290, 0.17676, 0.17202, 0.18016, 0.18098],
    "haberman": [0.17612, 0.18368, 0.17867, 0.31276, 0.19870, 0.20477, 0.26332],
    "segment0": [0.01048, 0.00362, 0.00738, 0.00188, 0.00644, 0.01023, 0.00507],
    "ecoli0345": [0.03727, 0.05425, 0.05506, 0.05044, 0.04556, 0.05739, 0.04792],
    "vowel0": [0.02448, 0.01959, 0.01796, 0.01858, 0.02548, 0.02711, 0.04561],
}

calibration_loss = {
    "wisconsin": [0.00657, 0.00906, 0.00813, 0.01361, 0.00842, 0.00921, 0.01098],
    "glass0": [0.02193, 0.04284, 0.03958, 0.03788, 0.03893, 0.03807, 0.04539],
    "haberman": [0.01654, 0.02184, 0.01799, 0.12724, 0.04014, 0.04166, 0.08679],
    "segment0": [0.00647, 0.00007, 0.00012, 0.00004, 0.00040, 0.00089, 0.00014],
    "ecoli0345": [0.01962, 0.01885, 0.02237, 0.01657, 0.01733, 0.02424, 0.01280],
    "vowel0": [0.00656, 0.00577, 0.00415, 0.00352, 0.00973, 0.01324, 0.00524],
}

auc_scores = {
    "wisconsin": [0.99597, 0.99572, 0.99529, 0.99301, 0.99422, 0.99515, 0.99077],
    "glass0": [0.81107, 0.80853, 0.81152, 0.80221, 0.82353, 0.81672, 0.80487],
    "haberman": [0.69776, 0.65641, 0.67929, 0.61919, 0.66894, 0.65025, 0.62733],
    "segment0": [0.99785, 0.49236, 0.58165, 0.39720, 0.69134, 0.89009, 0.68938],
    "ecoli0345": [0.93765, 0.84090, 0.86636, 0.81296, 0.57299, 0.79059, 0.86682],
    "vowel0": [0.99036, 0.99325, 0.99338, 0.98184, 0.99372, 0.99313, 0.84329],
}

# Function to print results
def print_results(metric_name, metric_values):
    print(f"\nTable: RESULTS ON THE DATASETS IN TERMS OF {metric_name.upper()}.")
    print("DATASET    " + " ".join([f"{model:<12}" for model in models]))
    for dataset in datasets:
        values = " ".join([f"{val:.5f}" for val in metric_values[dataset]])
        print(f"{dataset:<10} {values}")

# Print all results
print_results("Brier Score", brier_scores)
print_results("Calibration Loss", calibration_loss)
print_results("AUC Score", auc_scores)
