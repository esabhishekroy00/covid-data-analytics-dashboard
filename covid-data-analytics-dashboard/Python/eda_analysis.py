import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("../data/covid_cleaned.csv")

# Global cases per day
global_cases = df.groupby("date")["total_cases"].sum()

plt.figure(figsize=(10,5))
plt.plot(global_cases)
plt.title("Global COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.show()

# Top 10 countries by total cases
top_countries = df.groupby("country")["total_cases"].max().sort_values(ascending=False).head(10)

print("\nTop 10 Countries by COVID Cases:")
print(top_countries)

# Bar chart
top_countries.plot(kind="bar")

plt.title("Top 10 Countries by Total Cases")
plt.ylabel("Cases")
plt.xticks(rotation=45)

plt.show()