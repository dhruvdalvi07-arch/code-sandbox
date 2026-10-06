import numpy as np
import pandas as pd

# 1. NumPy: High-speed arrays and vector math
prices = np.array([120, 250, 400, 150, 600])
discounted = prices * 0.90  # 10% discount applied to all instantly!

print("=== NumPy Output ===")
print("Original Prices:", prices)
print("After 10% Discount:", discounted)
print("Average Price:", np.mean(discounted))

# 2. Pandas: Structured data tables (DataFrames)
data = {
    "Item": ["Earbuds", "Laptop Bag", "Monitor", "Keyboard", "Desk Chair"],
    "Original_Price": prices,
    "Discounted_Price": discounted,
}

df = pd.DataFrame(data)
df["Savings"] = df["Original_Price"] - df["Discounted_Price"]

print("\n=== Pandas DataFrame ===")
print(df)
