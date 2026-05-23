import pandas as pd
import sqlite3

df = pd.read_csv("construction_costs_clean.csv")

conn = sqlite3.connect("construction_costs.db")

df.to_sql("costs", conn, if_exists="replace", index=False)

print("Database created successfully!")
print(f"Table 'costs' loaded with {len(df)} rows.")
queries = {
    "avg_cost_by_city": """
        SELECT City, 
               ROUND(AVG(Unit_Cost_NGN), 2) AS Avg_Cost
        FROM costs
        GROUP BY City
        ORDER BY Avg_Cost DESC
    """,
    "avg_cost_by_item": """
        SELECT Item,
               ROUND(AVG(Unit_Cost_NGN), 2) AS Avg_Cost
        FROM costs
        GROUP BY Item
        ORDER BY Avg_Cost DESC
    """,
    "avg_cost_by_year": """
        SELECT Year,
               ROUND(AVG(Unit_Cost_NGN), 2) AS Avg_Cost
        FROM costs
        GROUP BY Year
        ORDER BY Year ASC
    """,
    "avg_cost_by_region": """
        SELECT Region,
               ROUND(AVG(Unit_Cost_NGN), 2) AS Avg_Cost
        FROM costs
        GROUP BY Region
        ORDER BY Avg_Cost DESC
    """,
    "material_vs_labour": """
        SELECT Cost_Category,
               ROUND(AVG(Unit_Cost_NGN), 2) AS Avg_Cost,
               COUNT(*) AS Number_of_Items
        FROM costs
        GROUP BY Cost_Category
        ORDER BY Avg_Cost DESC
    """,
    "top_price_increases": """
        SELECT City,
               Item,
               MAX(Unit_Cost_NGN) - MIN(Unit_Cost_NGN) AS Price_Increase,
               MIN(Unit_Cost_NGN) AS Cost_2023,
               MAX(Unit_Cost_NGN) AS Cost_2025,
               ROUND((MAX(Unit_Cost_NGN) - MIN(Unit_Cost_NGN)) * 100.0 / MIN(Unit_Cost_NGN), 2) AS Pct_Increase
        FROM costs
        GROUP BY City, Item
        ORDER BY Pct_Increase DESC
        LIMIT 10
    """
}

for name, query in queries.items():
    result = pd.read_sql_query(query, conn)
    result.to_csv(f"{name}.csv", index=False)
    print(f"Saved: {name}.csv")

print("\nAll query results saved successfully!")