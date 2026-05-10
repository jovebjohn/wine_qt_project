import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_heatmap(df):
    plt.figure(figsize=(12, 8))

    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

    plt.title("Correlation Heatmap")

    plt.show()

def plot_quality_distribution(df):
    plt.figure(figsize=(8, 5))

    sns.countplot(x='quality', data=df)

    plt.title("Wine Quality Distribution")

    plt.show()