
import pandas as pd

# Sample data with missing values
data = {
    "Name": ["Avi", "Anish", None, "Dev"],
    "Age": [25, None, 30, 22]
}

df = pd.DataFrame(data)

# Fill missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df)