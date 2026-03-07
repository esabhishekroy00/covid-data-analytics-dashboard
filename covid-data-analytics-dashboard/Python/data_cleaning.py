import pandas as pd

# Load dataset
df = pd.read_csv("../data/owid-covid-data.csv")

print("Dataset Loaded Successfully\n")

# Show dataset info
print("Columns in dataset:")
print(df.columns)

# Rename columns for easier use
df = df.rename(columns={
    "Date": "date",
    "Country/Region": "country",
    "Confirmed": "total_cases",
    "Deaths": "total_deaths",
    "Recovered": "recovered",
    "Active": "active_cases"
})

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Fill missing values
df.fillna(0, inplace=True)

# Save cleaned dataset
df.to_csv("../data/covid_cleaned.csv", index=False)

print("\nData cleaning completed.")
print("Clean dataset saved as covid_cleaned.csv")