# -*- coding: utf-8 -*-
"""SCT_DS_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/171wTp-XrNzX7Chavki46rNqHHEwZJkEw

**🎯Task 1: Visualizing Categorical and Continuous Variable Distributions**

In this task, we aim to create visualizations that help us understand the distribution of both categorical and continuous variables using a real-world dataset.

We selected a modern and engaging dataset containing metadata about Spotify songs, including attributes such as genre, popularity, and duration. The visualizations created will help uncover:

The most common music genres (categorical variable)
The spread and frequency of song popularity scores (continuous variable)
This task demonstrates fundamental EDA (Exploratory Data Analysis) techniques using Python libraries like Pandas, Seaborn, and Matplotlib.
"""

#AKASH_TASK_1
#SCT_DS_1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/SpotifyFeatures.CSV")

df.head()

df.columns

# Categorical Variable
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import numpy as np

colors = cm.viridis(np.linspace(0, 1, len(df['genre'].unique())))

plt.figure(figsize=(12, 8))
ax = sns.countplot(
    y='genre',
    data=df,
    order=df['genre'].value_counts().index,
    color='skyblue',
    edgecolor='black'
)

for i, bar in enumerate(ax.patches):
    bar.set_facecolor(colors[i])

plt.title('Distribution of Song Genres', fontsize=16, fontweight='bold')
plt.ylabel('Genre', fontsize=12)
plt.xlabel('Count', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()

for p in ax.patches:
    width = p.get_width()
    ax.text(width + 0.5, p.get_y() + p.get_height()/2.,
            int(width), ha='left', va='center', fontsize=10, color='black')

plt.show()

# Continuous Variable
plt.figure(figsize=(12, 6))
ax = sns.histplot(df['popularity'], bins=5, edgecolor='black', color='skyblue')

colors = cm.coolwarm(np.linspace(0, 1, len(ax.patches)))

for i, patch in enumerate(ax.patches):
    patch.set_facecolor(colors[i])

plt.title('Distribution of Song Popularity', fontsize=16, fontweight='bold')
plt.xlabel('Popularity Score', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()

for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width()/2., height + 0.5,
            int(height), ha='center', va='bottom', fontsize=10, color='black')

plt.show()

"""🔍 **Insights from Task 1**
-------------------------------------------
After analyzing the Spotify dataset:

Top Genres: Comedy, Soundtrack, Indie, and Jazz were the most frequent genres, each appearing over 9,000 times. This suggests a strong representation of these categories in the dataset.

Popularity Distribution: Most songs had popularity scores ranging from 20 to 80, with the majority concentrated between 40 and 60. Only a small number of songs were in the 0–20 or 80–100 extremes.

These insights can help in understanding listener preferences, content diversity, and how popularity is distributed across tracks in a large music library.
"""