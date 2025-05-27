# 🧬 Interactive Volcano Plot Customizer

This repository provides a **live, interactive volcano plot customizer** for visualizing differentially expressed genes. Upload your Excel data and watch the plot update in real-time as you adjust parameters!

## ✨ Key Features

- **🔴 Live Interactive Customizer**: Real-time volcano plot generation with instant updates
- **📁 Excel Upload Support**: Direct drag-and-drop Excel file processing
- **🎨 Full Customization**: Colors, thresholds, point sizes, and transparency
- **📊 Live Statistics**: Real-time gene counts and percentages
- **💾 Export Options**: PNG, SVG, and interactive HTML formats
- **📈 Sample Data**: Built-in demo data to try it immediately

## 🚀 Quick Start

### ⭐ **FASTEST WAY TO START:**
- **Windows**: Double-click `start_volcano_customizer.bat`
- **Any OS**: Open `index.html` in your browser for the main menu

### ⭐ **MAIN FEATURE: Live Interactive Customizer**
1. Open `Create Working with Html/live_volcano_customizer.html` in your web browser
2. **Option A**: Click "Upload Excel File" and drag your Excel data, or
3. **Option B**: Click "Use Sample Data" to see it in action immediately
4. Adjust any parameters and watch the plot update in real-time!
5. Export your customized plot in your preferred format

### Alternative Options
- **Python Script**: Run `Create with Excel and python/working_volcano.py` for static plot generation
- **Jupyter Analysis**: Use `Create with Excel and python/volcano_plot_analysis.ipynb` for detailed analysis

## 📊 Understanding Volcano Plots
- **X-axis**: log₂(Fold Change) - magnitude of expression change
- **Y-axis**: -log₁₀(P-value) - statistical significance  
- **🔴 Red points**: Upregulated genes (higher expression)
- **🔵 Blue points**: Downregulated genes (lower expression)
- **⚪ Gray points**: Non-significant genes

## 📁 Project Structure

### 🚀 **Quick Access Files**
- **`index.html`** - Main menu and project overview
- **`start_volcano_customizer.bat`** - Windows quick-start script

### 🌐 **Create Working with Html/** (⭐ MAIN FEATURES)
- **`live_volcano_customizer.html`** - Live interactive volcano plot customizer
- **`volcano_plot_customizer.html`** - Python code generator with controls

### 🐍 **Create with Excel and python/**  
- **`working_volcano.py`** - Static plot generation script
- **`volcano_plot_analysis.ipynb`** - Jupyter notebook analysis
- **`volcano_plot_MG72_vs_MG24_complete_dataset.png/pdf`** - Publication-ready plots

### 📈 **Data for Making Graph/**
- **`MG72VSMG24_Gene_differential_expression.xlsx`** - Complete dataset (17,437 genes)

## 📊 Dataset Results (MG72 vs MG24)

From the complete gene expression analysis:

- **Total genes analyzed**: 17,437
- **Upregulated genes**: 2,491 (14.3%)
- **Downregulated genes**: 6,326 (36.3%)
- **Non-significant genes**: 8,620 (49.4%)
- **Total significant genes**: 8,817 (50.6%)

### Analysis Parameters
- **Fold Change threshold**: ±2.0 (log₂FC: ±1.00)
- **P-value threshold**: 0.05 (-log₁₀: 1.30)

## 💻 Technical Requirements

### For HTML Interactive Tools
- Any modern web browser (Chrome, Firefox, Safari, Edge)
- No additional installations required!

### For Python Scripts
```bash
pip install pandas matplotlib numpy seaborn openpyxl
```

## 📊 Data Format Support

The tools support Excel files (.xlsx) with the following expected columns:
- `gene_name` or `gene_id`: Gene identifier
- `log2(fc)`: Log₂ fold change values  
- `pval`: P-value for statistical significance

The live customizer automatically detects column names and provides helpful error messages for any formatting issues.

## 🎨 Customization Options

### Live Interactive Features
- **Colors**: Upregulated, downregulated, and non-significant gene colors
- **Thresholds**: Fold change and p-value significance cutoffs
- **Point Settings**: Size, transparency, and outline options
- **Labels**: Custom axis labels and title
- **Export**: PNG, SVG, and interactive HTML formats

### Python Script Features
- High-resolution output (300 DPI)
- Publication-ready formatting
- Statistical summary boxes
- Customizable color schemes
- Multiple export formats

## 🔧 Troubleshooting

**Excel Upload Issues:**
- Ensure your Excel file has the expected column names
- Check that data is in the first sheet
- Verify numeric data in log2(fc) and pval columns

**Performance:**
- For large datasets (>10,000 genes), the tool automatically samples data for smooth interaction
- Use the Python scripts for processing very large datasets

## 📖 Citation

If you use this tool in your research, please cite:
```
Interactive Volcano Plot Customizer
GitHub: https://github.com/[username]/Volcano-Plots-of-Upregulated-and-Downregulated-Genes-for-Each-Comparison
```

---
*Last updated: May 28, 2025*
