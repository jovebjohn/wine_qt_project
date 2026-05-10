print("Running EDA Analysis...")

from load_data import load_dataset
from basic_info import show_basic_info
from data_statistics import show_statistics
from visualization import (
    plot_correlation_heatmap,
    plot_quality_distribution
)

# Load dataset
df = load_dataset('data/WineQT.csv')

# Show information
show_basic_info(df)

# Show statistics
show_statistics(df)

# Visualizations
plot_correlation_heatmap(df)

plot_quality_distribution(df)