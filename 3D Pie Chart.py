import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# Load the dataset
download_url = (
    "https://raw.githubusercontent.com/fivethirtyeight/"
    "data/master/college-majors/recent-grads.csv"
)

df = pd.read_csv(download_url)

# Extract the top 6 majors based on the number of graduates
top_majors = df.nlargest(6, 'Total')

# Creating dataset for the pie chart
majors = top_majors['Major'].tolist()
graduates = top_majors['Total'].tolist()

# Creating explode data
explode = [0.1] + [0.0] * (len(majors) - 1)

# Creating color parameters (you can customize this as needed)
colors = plt.cm.Paired(np.linspace(0, 1, len(majors)))

# Wedge properties
wp = {'linewidth': 1, 'edgecolor': "green"}

# Creating autocpt arguments
def func(pct, allvalues):
    absolute = int(pct / 100. * np.sum(allvalues))
    return "{:.1f}%\n({:d})".format(pct, absolute)

# Creating plot
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(graduates,
                                  autopct=lambda pct: func(pct, graduates),
                                  explode=explode,
                                  labels=majors,
                                  shadow=True,
                                  colors=colors,
                                  startangle=90,
                                  wedgeprops=wp,
                                  textprops=dict(color="magenta"))

# Adding legend
ax.legend(wedges, majors,
          title="Majors",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Top 6 College Majors by Number of Graduates")

# Show Plot
plt.show()

print("Carlos Vejar")