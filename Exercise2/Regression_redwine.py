import pandas as pd
import matplotlib.pyplot as plt

# Load the red wine dataset from the Exercise2 folder

df = pd.read_csv('Exercise2/winequality-red.csv')

# Print the counts of each wine quality value so we can see the target distribution
counts = df['quality'].value_counts()
print(counts)


# Group wines into three quality ranges so the histograms are easier to compare
quality_groups = {
    'Low quality (<=4)': df[df['quality'] <= 4],
    'Medium quality (5-6)': df[(df['quality'] >= 5) & (df['quality'] <= 6)],
    'High quality (>=7)': df[df['quality'] >= 7],
}

# Define a function that draws a histogram for one feature
# and shows how that feature is distributed for each quality group.


def plot_hist(feature, xlabel):
    plt.figure(figsize=(8, 4))
    for label, group in quality_groups.items():
        plt.hist(group[feature], bins=20, alpha=0.5, label=label, density=True)
    plt.title(f'{feature} distribution by wine quality')
    plt.xlabel(xlabel)
    plt.ylabel('Density')
    plt.legend()
    plt.tight_layout()
    plt.show()


# Draw the four histograms.
plot_hist('alcohol', 'Alcohol (%)')
plot_hist('density', 'Density')
plot_hist('pH', 'pH')
plot_hist('total sulfur dioxide', 'Total sulfur dioxide')
