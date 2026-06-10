"""
Reference solution: Boxplot + t-test with significance annotation
Dataset: Palmer Penguins (penguins.csv)
Compares flipper length between Adelie and Chinstrap penguins.
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# ── 1. Load and filter data ───────────────────────────────────────────────────

df = pd.read_csv('penguins.csv')

# Keep only the two species we want to compare
df = df[df['species'].isin(['Adelie', 'Chinstrap'])]

# Drop rows missing the measurement we're analyzing
df = df.dropna(subset=['flipper_length_mm'])

# Separate into two groups for the t-test
adelie = df[df['species'] == 'Adelie']['flipper_length_mm']
chinstrap = df[df['species'] == 'Chinstrap']['flipper_length_mm']

# ── 2. Run independent samples t-test ────────────────────────────────────────

t_stat, p_value = stats.ttest_ind(adelie, chinstrap)

# Assign significance stars based on p-value thresholds
if p_value < 0.001:
    stars = '***'
elif p_value < 0.01:
    stars = '**'
elif p_value < 0.05:
    stars = '*'
else:
    stars = 'ns'

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value:     {p_value:.6f}")
print(f"Significance: {stars}")

# ── 3. Create the boxplot ─────────────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(6, 7))

colors = ['#4C8BE0', '#E07D4C']  # blue for Adelie, orange for Chinstrap

bp = ax.boxplot(
    [adelie, chinstrap],
    tick_labels=['Adelie', 'Chinstrap'],
    patch_artist=True,           # needed to fill boxes with color
    widths=0.45,
    medianprops=dict(color='white', linewidth=2.5),
    whiskerprops=dict(linewidth=1.5),
    capprops=dict(linewidth=1.5),
    flierprops=dict(marker='o', markersize=4, alpha=0.5)
)

# Apply colors to boxes and outlier markers
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)

for flier, color in zip(bp['fliers'], colors):
    flier.set_markerfacecolor(color)
    flier.set_markeredgecolor(color)

# ── 4. Draw significance bracket and annotation ───────────────────────────────

# Position the bracket just above the highest data point (including outliers)
y_max = max(adelie.max(), chinstrap.max())
y_bracket = y_max + 3    # bottom of the bracket lines
bar_height = 1.5          # how tall the vertical parts of the bracket are
y_text = y_bracket + bar_height + 0.5  # where the text sits

# Draw the bracket: two vertical lines connected by a horizontal bar
# x positions 1 and 2 correspond to the two boxplot groups
ax.plot(
    [1, 1, 2, 2],
    [y_bracket, y_bracket + bar_height, y_bracket + bar_height, y_bracket],
    color='black', linewidth=1.5
)

# Annotate with stars and numeric p-value centered over the bracket
ax.text(
    1.5, y_text,
    f'{stars}\np = {p_value:.4f}',
    ha='center', va='bottom',
    fontsize=12, fontweight='bold'
)

# ── 5. Labels, styling, and save ─────────────────────────────────────────────

ax.set_ylabel('Flipper Length (mm)', fontsize=13)
ax.set_title('Flipper Length: Adelie vs Chinstrap Penguins',
             fontsize=13, fontweight='bold')

# Extend y-axis to give the annotation room
ax.set_ylim(170, y_text + 12)

# Remove top and right spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(labelsize=11)

plt.tight_layout()
plt.savefig('Claude_penguins_boxplot_ttest.png', dpi=150, bbox_inches='tight')
print("Figure saved as Claude_penguins_boxplot_ttest.png")
