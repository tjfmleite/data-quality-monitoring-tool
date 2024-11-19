import pandas as pd


data = pd.read_csv("data_quality.csv")


print("Dataset Overview:")
print(data)

# Missing Values
missing_values = data.isnull().sum()
print("\nMissing Values by Column:")
print(missing_values)

# Identify Negative or Invalid Values
# Invalid ages
invalid_ages = data[(data["Age"] < 0) | (data["Age"] > 100)]

# Negative balances
negative_balances = data[data["Balance"] < 0]

# Generating Summary Statistics
summary = data.describe(include="all")
print("\nSummary Statistics:")
print(summary)


with open("data_quality_report.txt", "w") as report:
    report.write("Data Quality Report\n")
    report.write("====================\n\n")
    report.write("Missing Values:\n")
    report.write(missing_values.to_string())
    report.write("\n\nInvalid Ages:\n")
    report.write(invalid_ages.to_string())
    report.write("\n\nNegative Balances:\n")
    report.write(negative_balances.to_string())
    report.write("\n\nSummary Statistics:\n")
    report.write(summary.to_string())

print("\nData quality report has been saved to 'data_quality_report.txt'.")
