import pandas as pd

cities = [
    "Lagos", "Abuja", "Port Harcourt", "Ibadan", "Ogun",
    "Kano", "Enugu", "Kaduna", "Benin City", "Owerri"
]

items = [
    "Cement (50kg bag)",
    "Concrete Blocks (9-inch)",
    "Steel Bars (per kg)",
    "Sand (per ton)",
    "Granite (per ton)",
    "Formwork (per m²)",
    "Daily Labour"
]

years = [2023, 2024, 2025]

prices = {
    "Cement (50kg bag)": {
        "Lagos":         [3800, 6800, 9800],
        "Abuja":         [4200, 7000, 10200],
        "Port Harcourt": [4000, 6500, 9500],
        "Ibadan":        [3500, 6200, 9000],
        "Ogun":          [3600, 6300, 9100],
        "Kano":          [3400, 6000, 8800],
        "Enugu":         [3700, 6400, 9300],
        "Kaduna":        [3300, 5900, 8600],
        "Benin City":    [3600, 6300, 9200],
        "Owerri":        [3700, 6500, 9400]
    },
    "Concrete Blocks (9-inch)": {
        "Lagos":         [600, 800, 950],
        "Abuja":         [550, 750, 880],
        "Port Harcourt": [520, 720, 850],
        "Ibadan":        [480, 680, 800],
        "Ogun":          [500, 700, 820],
        "Kano":          [450, 650, 780],
        "Enugu":         [470, 670, 800],
        "Kaduna":        [440, 640, 760],
        "Benin City":    [480, 680, 810],
        "Owerri":        [490, 690, 820]
    },
    "Steel Bars (per kg)": {
        "Lagos":         [480, 700, 1050],
        "Abuja":         [490, 710, 1060],
        "Port Harcourt": [470, 690, 1040],
        "Ibadan":        [450, 670, 1020],
        "Ogun":          [460, 680, 1030],
        "Kano":          [440, 660, 1000],
        "Enugu":         [460, 675, 1020],
        "Kaduna":        [430, 650, 990],
        "Benin City":    [455, 670, 1010],
        "Owerri":        [465, 680, 1025]
    },
    "Sand (per ton)": {
        "Lagos":         [4500, 6500, 8000],
        "Abuja":         [4200, 6200, 7800],
        "Port Harcourt": [4000, 6000, 7500],
        "Ibadan":        [3500, 5500, 7000],
        "Ogun":          [3600, 5600, 7100],
        "Kano":          [3200, 5200, 6800],
        "Enugu":         [3700, 5700, 7200],
        "Kaduna":        [3100, 5100, 6600],
        "Benin City":    [3600, 5600, 7100],
        "Owerri":        [3800, 5800, 7300]
    },
    "Granite (per ton)": {
        "Lagos":         [5500, 7500, 9500],
        "Abuja":         [5200, 7200, 9200],
        "Port Harcourt": [6000, 8000, 10000],
        "Ibadan":        [5000, 7000, 9000],
        "Ogun":          [5100, 7100, 9100],
        "Kano":          [4500, 6500, 8500],
        "Enugu":         [5200, 7200, 9200],
        "Kaduna":        [4400, 6400, 8400],
        "Benin City":    [5100, 7100, 9100],
        "Owerri":        [5300, 7300, 9300]
    },
    "Formwork (per m²)": {
        "Lagos":         [1800, 2800, 3800],
        "Abuja":         [1700, 2700, 3700],
        "Port Harcourt": [1600, 2600, 3600],
        "Ibadan":        [1500, 2500, 3400],
        "Ogun":          [1500, 2500, 3400],
        "Kano":          [1400, 2400, 3200],
        "Enugu":         [1500, 2500, 3400],
        "Kaduna":        [1300, 2300, 3100],
        "Benin City":    [1500, 2500, 3400],
        "Owerri":        [1550, 2550, 3500]
    },
    "Daily Labour": {
        "Lagos":         [2500, 3500, 5000],
        "Abuja":         [2500, 3500, 5000],
        "Port Harcourt": [2300, 3300, 4800],
        "Ibadan":        [2000, 3000, 4500],
        "Ogun":          [2000, 3000, 4500],
        "Kano":          [1800, 2800, 4200],
        "Enugu":         [2000, 3000, 4500],
        "Kaduna":        [1800, 2800, 4200],
        "Benin City":    [2000, 3000, 4500],
        "Owerri":        [2100, 3100, 4600]
    }
}
rows = []

for item in items:
    for city in cities:
        for i, year in enumerate(years):
            rows.append({
                "City": city,
                "Item": item,
                "Year": year,
                "Unit_Cost_NGN": prices[item][city][i]
            })
df = pd.DataFrame(rows)
print(df)
print(f"\nTotal rows: {len(df)}")
df.to_csv("construction_costs.csv", index=False)
print("Dataset saved successfully!")