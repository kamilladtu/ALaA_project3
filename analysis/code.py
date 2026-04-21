import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/brorbruland/Desktop/ALaA_project3/data_2228 (1).csv", index_col=0)

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm", center=0)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=150)
plt.show()

# Pairplot
sns.pairplot(df)
plt.savefig("pairplot.png", dpi=150)
plt.show()