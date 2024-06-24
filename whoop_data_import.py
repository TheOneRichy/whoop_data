import pandas as pd

# Read the CSV file
file_path = "workouts.csv"
df = pd.read_csv(file_path)

print(df.head())