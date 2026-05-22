import pandas as pd

df = pd.read_csv("construction_costs.csv")
print(df.head(10))
print(f"\nShape: {df.shape}")
print(f"\nColumns: {df.columns.tolist()}")
print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

print("\nBasic Statistics:")
print(df["Unit_Cost_NGN"].describe())
region_map = {
    "Lagos": "South West",
    "Ogun": "South West",
    "Ibadan": "South West",
    "Abuja": "North Central",
    "Kaduna": "North West",
    "Kano": "North West",
    "Enugu": "South East",
    "Owerri": "South East",
    "Port Harcourt": "South South",
    "Benin City": "South South"
}

category_map = {
    "Cement (50kg bag)": "Material",
    "Concrete Blocks (9-inch)": "Material",
    "Steel Bars (per kg)": "Material",
    "Sand (per ton)": "Material",
    "Granite (per ton)": "Material",
    "Formwork (per m²)": "Material",
    "Daily Labour": "Labour"
}

df["Region"] = df["City"].map(region_map)
df["Cost_Category"] = df["Item"].map(category_map)

print("\nUpdated Columns:")
print(df.head(10))
print(f"\nRegions: {df['Region'].unique()}")
print(f"\nCategories: {df['Cost_Category'].unique()}")
df.to_csv("construction_costs_clean.csv", index=False)
print("\nClean dataset saved successfully!")