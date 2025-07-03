import pandas as pd

# Replace with your actual CSV filename
input_file = "C:\\Users\\juhkem\\Downloads\\Crimes_-_2001_to_Present_20250603.csv"
output_file = "C:\\Users\\juhkem\\Downloads\\chicago_crimes_2025_2025.csv"

# Read the dataset
df = pd.read_csv(input_file)

# Show total number of rows in the original file
print(f"Total rows in original file: {len(df)}")

# Filter for years 2020 to 2025
df_filtered = df[df['Year'].between(2025, 2025)]

# Remove 'Case Number' column if it exists
if 'Case Number' in df_filtered.columns:
    df_filtered = df_filtered.drop(columns=['Case Number'])
    
if 'IUCR' in df_filtered.columns:
    df_filtered = df_filtered.drop(columns=['IUCR'])

if 'Community Area' in df_filtered.columns:
    df_filtered = df_filtered.drop(columns=['Community Area'])

if 'District' in df_filtered.columns:
    df_filtered = df_filtered.drop(columns=['District'])

if 'FBI code' in df_filtered.columns:
    df_filtered = df_filtered.drop(columns=['FBI code'])

if 'Updated On' in df_filtered.columns:
    df_filtered = df_filtered.drop(columns=['Updated On'])

if 'Ward' in df_filtered.columns:
    df_filtered = df_filtered.drop(columns=['Ward'])

if 'X Coordinate' in df_filtered.columns:
    df_filtered = df_filtered.drop(columns=['X Coordinate'])

if 'Y Coordinate' in df_filtered.columns:
    df_filtered = df_filtered.drop(columns=['Y Coordinate'])

# Show number of rows after filtering
print(f"Rows from 2025 to 2025: {len(df_filtered)}")

# Save to new CSV
df_filtered.to_csv(output_file, index=False)