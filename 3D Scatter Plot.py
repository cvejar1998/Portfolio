# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# File ID from Google Drive link
file_id = '1zV-ysQwW7r_YUd0y4KwmEJukAtA54WnK'

# Construct the download URL
url = f'https://drive.google.com/uc?id={file_id}'

# Read the CSV file into a DataFrame
df = pd.read_csv(url)

# Extracting x, y, z data from the DataFrame
x_values = df['Popularity'].values
y_values = df['Danceability'].values
z_values = df['Key'].values

# Creating figure
fig = plt.figure(figsize=(10, 7))
ax = plt.axes(projection="3d")

# Creating 3D scatter plot
ax.scatter3D(x_values, y_values, z_values, color="red")

# Adding title and labels
plt.title("Classic Disco 3D Scatter")
ax.set_xlabel('Popularity')
ax.set_ylabel('Danceability')
ax.set_zlabel('Key')

# Fixes Z axis Label being cut off
ax.set_box_aspect(None, zoom=0.85)


# Show plot
plt.show()