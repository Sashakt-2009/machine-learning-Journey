# EDA Report Generator

A simple exploratory data analysis (EDA) script for CSV datasets, built with Python, pandas, NumPy, and Matplotlib.

## What it does

- Reads a dataset from `datasets/iris.csv`
- Prints dataset summary information
- Detects numeric and categorical columns
- Generates:
  - Histogram plot for numeric columns
  - Scatter plots for numeric column pairs
  - Pie charts for categorical columns
- Saves plot images to `Saves/`

## Project structure

- `mains.py` - main script that performs the EDA and saves plots
- `datasets/iris.csv` - sample dataset used by the script
- `Saves/` - output folder for generated plot images

## Requirements

- Python 3.x
- pandas
- NumPy
- Matplotlib

## Installation

1. Create and activate a Python virtual environment(recomended)

2. Install dependencies:

```powershell
pip install pandas numpy matplotlib
```

## Usage

Run the script from the workspace root directory:

```powershell
python "EDA report generator\mains.py"
```

After execution, the generated images will be saved to:

- `EDA report generator/Saves/histogram.png`
- `EDA report generator/Saves/scatterplot.png`
- `EDA report generator/Saves/piechart.png`

## Notes

- The script currently expects the CSV file path to be `EDA report generator/datasets/iris.csv`.
- It is designed for datasets containing numeric (`float64`) and string (`str`) columns.
- You can replace the dataset with another CSV file, but you may need to adjust the data path and column handling if the file format differs.
