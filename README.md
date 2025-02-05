# GEV Regression Project

## Overview
This project demonstrates the implementation of **GEV Regression** and compares it with other methods such as LOGIT, PROBIT, and CLOGLOG. The project generates **log-loss graphs** across iterations for multiple datasets and calculates **Brier scores** to evaluate model performance.

### Key Features:
- **Graphical Representation**: Log-loss vs. iterations for each dataset.
- **Tabular Results**: Brier scores for different regression models across datasets.
- **Synthetic Data**: Simulates datasets for demonstration purposes (can be replaced with real data).

## Datasets
The project uses synthetic datasets to simulate various classification problems:
- `ecoli`
- `haberman`
- `glass0`
- `vowel0`
- `wisconsin`
- `segment0`

> You can replace these with your own datasets by modifying the `datasets` dictionary in the code.

## Outputs
1. **Graphs**: Log-loss graphs for gradient, Hessian, and proposed methods are saved as `log_loss_graphs.png`.
2. **Tabular Results**: Brier scores for regression methods are saved in `brier_scores.csv`.
3. **Dataset Samples**: Prints sample data from each dataset to the console for verification.

## Requirements
This project is written in Python and requires the following libraries:
- `numpy`
- `pandas`
- `matplotlib`

Install them using:
```bash
pip install numpy pandas matplotlib
