# Volcano Plots of Upregulated and Downregulated Genes

This repository contains code for creating volcano plots to visualize differentially expressed genes between MG72 and MG24 conditions.

## Overview

A volcano plot is a type of scatter plot that is used to quickly identify changes in large data sets composed of replicate data. It plots significance versus fold-change on the y and x axes, respectively.

### What the Plot Shows:
- **X-axis**: log₂(Fold Change) - indicates magnitude of expression change
- **Y-axis**: -log₁₀(P-value) - indicates statistical significance
- **Red points**: Upregulated genes (higher expression in MG72 vs MG24)
- **Cyan/Teal points**: Downregulated genes (lower expression in MG72 vs MG24)
- **Gray points**: Non-significant genes

## Files in this Repository

### Python Scripts
1. **`working_volcano.py`** - Main working script that generates the volcano plot
2. **`volcano_plot_analysis.ipynb`** - Jupyter notebook for interactive analysis
3. **`simple_volcano.py`** - Simplified version for testing
4. **`robust_volcano.py`** - Version with multiple encoding handling

### Data
- **`Data for Making Graph/`** - Contains the gene expression data
  - **`MG72VSMG24_genes_significantly_differential_expression.xlsx/Data.txt`** - Gene expression data file

### Output Files
- **`volcano_plot_MG72_vs_MG24.png`** - High-resolution PNG plot (300 DPI)
- **`volcano_plot_MG72_vs_MG24.pdf`** - Publication-ready PDF plot

## Results Summary

From the analysis of the gene expression data:

- **Total genes analyzed**: 15
- **Significantly differentially expressed**: 15 (100.0%)
- **Upregulated genes (MG72 > MG24)**: 11 (73.3%)
- **Downregulated genes (MG72 < MG24)**: 4 (26.7%)

### Significance Thresholds
- **Fold Change threshold**: ±2.0 (log₂FC: ±1.00)
- **P-value threshold**: 0.05 (-log₁₀: 1.30)

### Top Upregulated Genes
1. **Mn4_03848**: FC = 32.15, p < 0.01 - Uroporphyrin-III C-methyltransferase
2. **Mn4_08578**: FC = 20.90, p < 0.01 - Hypothetical protein
3. **Mn4_00256**: FC = 19.12, p < 0.01 - Glycerol/water channel protein
4. **Mn4_17519**: FC = 17.74, p < 0.01 - Hypothetical protein
5. **Mn4_05536**: FC = 16.00, p < 0.01 - Hypothetical protein

### Top Downregulated Genes
1. **Mn4_14323**: FC = 0.00, p < 0.01 - Fatty acid biosynthesis protein
2. **Mn4_11302**: FC = 0.00, p < 0.01 - Hypothetical protein
3. **Mn4_13634**: FC = 0.01, p < 0.01 - Acyltransferase/oxidoreductase
4. **Mn4_05378**: FC = 0.03, p < 0.01 - Hypothetical protein

# 🧬 Volcano Plot Analysis: MG72 vs MG24 Gene Expression

## 📊 Complete Dataset Analysis (Final Version)

This project generates volcano plots for differential gene expression analysis comparing MG72 vs MG24 conditions using the complete gene dataset.

### 🎯 **Current Working Files:**
- **`working_volcano.py`** - Main Python script for generating volcano plots
- **`volcano_plot_MG72_vs_MG24_complete_dataset.png`** - High-resolution volcano plot (300 DPI)
- **`volcano_plot_MG72_vs_MG24_complete_dataset.pdf`** - Publication-ready PDF version
- **`volcano_plot_analysis.ipynb`** - Jupyter notebook for interactive analysis
- **`README.md`** - This documentation file

### 📈 **Dataset Information:**
- **Source:** `Data for Making Graph/MG72VSMG24_Gene_differential_expression.xlsx`
- **Total genes analyzed:** 17,437
- **Comparison:** MG72 vs MG24 conditions

### 🔬 **Results Summary:**
- **Upregulated genes:** 2,491 (14.3%)
- **Downregulated genes:** 6,326 (36.3%)
- **Non-significant genes:** 8,620 (49.4%)
- **Total significant genes:** 8,817 (50.6%)

### 🏃‍♂️ **Quick Start:**
```bash
# Run the volcano plot analysis
python working_volcano.py
```

### 🎨 **Plot Features:**
- **Color coding:** Red (upregulated), Cyan (downregulated), Gray (non-significant)
- **Significance thresholds:** |log₂(FC)| ≥ 1.0, p-value ≤ 0.05
- **Statistics box:** Gene counts and percentages
- **High-quality output:** 300 DPI PNG + PDF formats

### 📋 **Requirements:**
- Python 3.x
- pandas
- matplotlib
- numpy
- seaborn
- openpyxl (for Excel file reading)

---
*Generated on May 28, 2025*

## Requirements

### Python Libraries
```bash
pip install pandas matplotlib numpy seaborn
```

### Required Packages
- `pandas` - Data manipulation and analysis
- `matplotlib` - Plotting library
- `numpy` - Numerical computing
- `seaborn` - Statistical data visualization

## Usage

### Running the Main Script
```bash
python working_volcano.py
```

### Using the Jupyter Notebook
1. Open `volcano_plot_analysis.ipynb` in Jupyter Notebook or JupyterLab
2. Run all cells to reproduce the analysis

### Script Features
- Automatic data loading and preprocessing
- Customizable significance thresholds
- High-quality plot generation (PNG and PDF)
- Statistical summary of results
- Publication-ready formatting

## Plot Interpretation

### Quadrants of the Volcano Plot
1. **Upper Right**: Significantly upregulated genes (high FC, low p-value)
2. **Upper Left**: Significantly downregulated genes (low FC, low p-value)
3. **Lower Middle**: Non-significant genes (any FC, high p-value)

### Key Elements
- **Dotted lines**: Significance thresholds for fold change and p-value
- **Color coding**: Easy identification of gene regulation status
- **Legend**: Shows count of genes in each category
- **Statistics box**: Summary of total and significant genes

## Customization

You can modify the following parameters in the script:

```python
# Significance thresholds
fc_threshold = 2.0          # Fold change threshold
pval_threshold = 0.05       # P-value threshold

# Plot appearance
colors = {
    'Not Significant': '#D3D3D3',  # Light gray
    'Upregulated': '#FF6B6B',      # Red
    'Downregulated': '#4ECDC4'     # Teal/cyan
}

# Figure size
fig, ax = plt.subplots(figsize=(12, 10))
```

## Data Format

The input data should be a tab-separated file with the following columns:
- `gene_id`: Unique gene identifier
- `gene_name`: Gene name
- `log2(fc)`: Log₂ fold change
- `pval`: P-value
- `regulation`: up/down regulation status
- Additional columns for FPKM values, annotations, etc.

## Citation

If you use this code in your research, please cite this repository:

```
Volcano Plots of Upregulated and Downregulated Genes for Each Comparison
GitHub Repository: https://github.com/[username]/Volcano-Plots-of-Upregulated-and-Downregulated-Genes-for-Each-Comparison
```

## License

This project is open source and available under the MIT License.

## Contact

For questions or issues, please open an issue in this repository.

---

**Note**: This analysis compares gene expression between MG72 and MG24 conditions. All genes in this dataset showed significant differential expression, indicating strong biological differences between the two conditions.
