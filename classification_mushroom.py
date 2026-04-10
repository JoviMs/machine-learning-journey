import pandas as pd
import matplotlib.pyplot as plt

# Load the mushroom dataset
df = pd.read_csv('mushrooms.csv')
counts = df['class'].value_counts()
print(counts)


df = pd.read_csv('mushrooms.csv')


# 1) Odor vs Class
odor = pd.crosstab(df['odor'], df['class'])
plt.bar(odor.index, odor['e'], label='Edible')
plt.bar(odor.index, odor['p'], bottom=odor['e'], label='Poisonous')
plt.title('Odor vs Class')
plt.xlabel('Odor')
plt.ylabel('Count')
plt.legend()
plt.show()
plt.close()

# 2) Spore Print Color vs Class
spore = pd.crosstab(df['spore-print-color'], df['class'])
plt.bar(spore.index, spore['e'], label='Edible')
plt.bar(spore.index, spore['p'], bottom=spore['e'], label='Poisonous')
plt.title('Spore Print Color vs Class')
plt.xlabel('Spore Print Color')
plt.ylabel('Count')
plt.legend()
plt.show()
plt.close()

# 3) Habitat vs Class
habitat = pd.crosstab(df['habitat'], df['class'])
plt.bar(habitat.index, habitat['e'], label='Edible')
plt.bar(habitat.index, habitat['p'], bottom=habitat['e'], label='Poisonous')
plt.title('Habitat vs Class')
plt.xlabel('Habitat')
plt.ylabel('Count')
plt.legend()
plt.show()
plt.close()

# 4) Cap Color vs Class
cap_color = pd.crosstab(df['cap-color'], df['class'])
plt.bar(cap_color.index, cap_color['e'], label='Edible')
plt.bar(cap_color.index, cap_color['p'],
        bottom=cap_color['e'], label='Poisonous')
plt.title('Cap Color vs Class')
plt.xlabel('Cap Color')
plt.ylabel('Count')
plt.legend()
plt.show()
plt.close()
