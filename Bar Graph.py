# Import libraries
import pandas as pd

# Load the dataset
download_url = (
    "https://raw.githubusercontent.com/fivethirtyeight/"
    "data/master/college-majors/recent-grads.csv"
)

df = pd.read_csv(download_url)

# DataFrame
type(df)

# Ensure all columns are displayed when viewing the DataFrame
pd.set_option("display.max.columns", None)

# Filter the dataset where the Median salary is greater than $60,000
# Sort by ascending order based on the Median salary
top_medians = df[df["Median"] > 60000].sort_values("Median")

# Plot a bar chart showing the 25th percentile (P25th), median, and 75th percentile (P75th) salaries
top_medians.plot(x="Major", y=["P25th", "Median", "P75th"], kind="bar")
