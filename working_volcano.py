import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set matplotlib backend to prevent hanging
import matplotlib
matplotlib.use('Agg')

def create_volcano_plot_from_excel():
    """Create volcano plot using data directly from Excel file"""
      # Read data from Excel file - Complete dataset with all genes
    excel_file = 'Data for Making Graph/MG72VSMG24_Gene_differential_expression.xlsx'
    
    print(f"Loading data from Excel file: {excel_file}")
    
    try:
        df = pd.read_excel(excel_file)
        print(f"✓ Data loaded successfully!")
        print(f"✓ Shape: {df.shape}")
        print(f"✓ Columns: {df.columns.tolist()[:10]}...")  # Show first 10 columns
        
        # Check for required columns
        required_cols = ['gene_name', 'log2(fc)', 'pval']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            print(f"❌ Missing required columns: {missing_cols}")
            return None
            
        # Select relevant columns and clean data
        df_clean = df[['gene_name', 'log2(fc)', 'pval']].copy()
        
        # Remove any rows with missing values
        original_count = len(df_clean)
        df_clean = df_clean.dropna()
        
        print(f"✓ After cleaning: {len(df_clean)} genes (removed {original_count - len(df_clean)} rows with missing data)")
        print("Data summary:")
        print(f"  - Fold change range: {df_clean['log2(fc)'].min():.3f} to {df_clean['log2(fc)'].max():.3f}")
        print(f"  - P-value range: {df_clean['pval'].min():.2e} to {df_clean['pval'].max():.3f}")
        print(f"  - Genes with p-value = 0: {(df_clean['pval'] == 0).sum()}")
        
        # Handle p-values of 0 (replace with a very small number for log transformation)
        df_clean['pval_adjusted'] = df_clean['pval'].replace(0, 1e-300)
        
        # Calculate -log10(p-value) for y-axis
        df_clean['-log10(pval)'] = -np.log10(df_clean['pval_adjusted'])
        
        # Define significance thresholds
        fc_threshold = 2.0  # Fold change threshold
        pval_threshold = 0.05  # P-value threshold
        log2fc_threshold = np.log2(fc_threshold)
        log10pval_threshold = -np.log10(pval_threshold)
        
        print(f"\nSignificance thresholds:")
        print(f"  Fold Change threshold: ±{fc_threshold} (log₂FC: ±{log2fc_threshold:.2f})")
        print(f"  P-value threshold: {pval_threshold} (-log₁₀: {log10pval_threshold:.2f})")
        
        # Categorize genes
        df_clean['category'] = 'Not Significant'
        upregulated = (df_clean['log2(fc)'] >= log2fc_threshold) & (df_clean['pval'] <= pval_threshold)
        downregulated = (df_clean['log2(fc)'] <= -log2fc_threshold) & (df_clean['pval'] <= pval_threshold)
        
        df_clean.loc[upregulated, 'category'] = 'Upregulated'
        df_clean.loc[downregulated, 'category'] = 'Downregulated'
        
        # Create the figure
        fig, ax = plt.subplots(figsize=(12, 10))
        
        # Define colors
        colors = {
            'Not Significant': '#D3D3D3',  # Light gray
            'Upregulated': '#FF6B6B',      # Red
            'Downregulated': '#4ECDC4'     # Teal/cyan
        }
        
        # Plot points by category
        for category in ['Not Significant', 'Downregulated', 'Upregulated']:
            subset = df_clean[df_clean['category'] == category]
            ax.scatter(subset['log2(fc)'], subset['-log10(pval)'], 
                      c=colors[category], alpha=0.6, s=30, 
                      label=f'{category} ({len(subset):,})', edgecolors='none')
        
        # Add threshold lines
        ax.axvline(x=log2fc_threshold, color='black', linestyle='--', alpha=0.7, linewidth=1)
        ax.axvline(x=-log2fc_threshold, color='black', linestyle='--', alpha=0.7, linewidth=1)
        ax.axhline(y=log10pval_threshold, color='black', linestyle='--', alpha=0.7, linewidth=1)
          # Customize the plot
        ax.set_xlabel('log₂(Fold Change)', fontsize=14, fontweight='bold')
        ax.set_ylabel('-log₁₀(P-value)', fontsize=14, fontweight='bold')
        ax.set_title('Volcano Plot: All Genes (Complete Dataset)\n(MG72 vs MG24 - 17,437 genes)', 
                    fontsize=16, fontweight='bold', pad=20)
        
        # Set axis limits with some padding
        x_max = max(abs(df_clean['log2(fc)'].min()), abs(df_clean['log2(fc)'].max())) * 1.1
        ax.set_xlim(-x_max, x_max)
        ax.set_ylim(0, df_clean['-log10(pval)'].max() * 1.1)
        
        # Add grid
        ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
        
        # Customize legend
        legend = ax.legend(loc='upper right', frameon=True, fancybox=True, shadow=True, fontsize=12)
        legend.get_frame().set_facecolor('white')
        legend.get_frame().set_alpha(0.9)
        
        # Add threshold annotations
        ax.text(log2fc_threshold + 0.1, ax.get_ylim()[1] * 0.95, 
               f'FC ≥ {fc_threshold}', rotation=90, fontsize=10, alpha=0.7)
        ax.text(-log2fc_threshold - 0.1, ax.get_ylim()[1] * 0.95, 
               f'FC ≤ {1/fc_threshold:.1f}', rotation=90, fontsize=10, alpha=0.7, ha='right')
        ax.text(ax.get_xlim()[1] * 0.95, log10pval_threshold + 0.1, 
               f'p ≤ {pval_threshold}', fontsize=10, alpha=0.7, ha='right')
        
        # Add statistics text box
        total_genes = len(df_clean)
        up_genes = len(df_clean[df_clean['category'] == 'Upregulated'])
        down_genes = len(df_clean[df_clean['category'] == 'Downregulated'])
        sig_genes = up_genes + down_genes
        
        stats_text = f'''Total genes: {total_genes:,}
Significant: {sig_genes:,} ({sig_genes/total_genes*100:.1f}%)
Upregulated: {up_genes:,}
Downregulated: {down_genes:,}'''
        
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, fontsize=11,
               verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        # Improve layout
        plt.tight_layout()
          # Save the plot - Complete dataset
        output_path = "volcano_plot_MG72_vs_MG24_complete_dataset.png"
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
        
        # Also save as PDF for publication
        pdf_path = "volcano_plot_MG72_vs_MG24_complete_dataset.pdf"
        plt.savefig(pdf_path, bbox_inches='tight', facecolor='white')
        
        # Close the figure
        plt.close()
        
        # Print summary statistics
        print("\n" + "="*60)
        print("VOLCANO PLOT SUMMARY (FROM EXCEL)")
        print("="*60)
        print(f"Total genes analyzed: {total_genes:,}")
        print(f"Significantly differentially expressed: {sig_genes:,} ({sig_genes/total_genes*100:.1f}%)")
        print(f"Upregulated genes (MG72 > MG24): {up_genes:,}")
        print(f"Downregulated genes (MG72 < MG24): {down_genes:,}")
        print(f"Fold change threshold: ±{fc_threshold}")
        print(f"P-value threshold: {pval_threshold}")
        
        if up_genes > 0:
            print("\nTop 10 upregulated genes:")
            top_up = df_clean[df_clean['category'] == 'Upregulated'].nlargest(10, 'log2(fc)')
            for i, (_, gene) in enumerate(top_up.iterrows(), 1):
                fc_actual = 2**gene['log2(fc)']
                print(f"  {i:2d}. {gene['gene_name']}: log2FC = {gene['log2(fc)']:7.3f}, FC = {fc_actual:8.2f}, p = {gene['pval']:.2e}")
        
        if down_genes > 0:
            print("\nTop 10 downregulated genes:")
            top_down = df_clean[df_clean['category'] == 'Downregulated'].nsmallest(10, 'log2(fc)')
            for i, (_, gene) in enumerate(top_down.iterrows(), 1):
                fc_actual = 2**gene['log2(fc)']
                print(f"  {i:2d}. {gene['gene_name']}: log2FC = {gene['log2(fc)']:7.3f}, FC = {fc_actual:8.2f}, p = {gene['pval']:.2e}")
        
        print(f"\nPlots saved as:")
        print(f"  PNG: {output_path}")
        print(f"  PDF: {pdf_path}")
        
        return df_clean
        
    except FileNotFoundError:
        print(f"❌ Error: Excel file not found: {excel_file}")
        print("Please make sure the file exists in the specified location.")
        return None
    except Exception as e:
        print(f"❌ Error loading Excel file: {e}")
        return None

if __name__ == "__main__":
    df = create_volcano_plot_from_excel()
    if df is not None:
        print("\n✓ Volcano plot analysis completed successfully!")
    else:
        print("\n❌ Volcano plot analysis failed!")
