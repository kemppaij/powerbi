import pandas as pd

# Replace with your actual CSV filename
input_file = "C:\\Users\\juhkem\\Downloads\\Crimes_-_2001_to_Present_20250603.csv"
output_file = "C:\\Users\\juhkem\\Downloads\\chicago_crimes_2020_2025.csv"

# Read the dataset
df = pd.read_csv(input_file)

# Filter for years 2020 to 2025
df_filtered = df[df['Year'].between(2020, 2025)]

# Save to new CSV
df_filtered.to_csv(output_file, index=False)