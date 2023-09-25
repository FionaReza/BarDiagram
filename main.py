import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Sample data
names = ['Moisture', 'Ash', 'Protein', 'Fat', 'Carbohydrate']
variable1 = [13, 27, 13.5, 1, 45]
variable2 = [10, 50, 13.6, 1, 25]

# Calculate the position of each bar on the x-axis
bar_width = 0.35
bar_positions = np.arange(len(names))

# Create the stacked bar graph with aligned bars
plt.bar(bar_positions, variable1, width=bar_width, label='S. binderi', color='lightgreen', alpha=0.8)
plt.bar(bar_positions, [-val for val in variable2], width=bar_width, label='P. pavonica', color='grey', alpha=0.8)

# Set axis labels and title
plt.xlabel('Parameters', fontname='Georgia', fontsize=12)
plt.ylabel('Percentage (%)', fontname='Georgia', fontsize=12)
plt.title('Results of Proximate Analysis', fontname='Georgia', fontsize=12)

# Set x-axis tick labels with italic font style
plt.xticks(bar_positions, names, fontname='Georgia', fontsize=12)

# Remove minus signs from y-axis labels
formatter = FuncFormatter(lambda x, pos: f'{abs(x):.0f}')
plt.gca().yaxis.set_major_formatter(formatter)

# Annotate the variable names in a box with italic font style
plt.annotate('S. binderi', (0.05, 0.9), xycoords='axes fraction', fontsize=12, fontstyle='italic', ha='left', bbox=dict(facecolor='white', edgecolor='lightgreen'))
plt.annotate('P. pavonica', (0.05, 0.82), xycoords='axes fraction', fontsize=12, fontstyle='italic', ha='left', bbox=dict(facecolor='white', edgecolor='grey'))

# Show the plot
plt.tight_layout()
plt.show()

