import pandas as pd

# Read the CSV file
file_path = "sleeps.csv"
sleep_data = pd.read_csv(file_path)


# Check for missing values
print(sleep_data.isnull().sum())

# Fill or drop missing values if necessary
sleep_data = sleep_data.dropna()

# Convert date columns to datetime objects if needed
sleep_data['date'] = pd.to_datetime(sleep_data['date'])