from pathlib import Path
import sys


# Give a clear installation instruction if Pandas is not available.
try:
    import pandas as pd
except ModuleNotFoundError as error:
    if error.name != "pandas":
        raise
    print(
        "Pandas is not installed. Install it with: pip install pandas",
        file=sys.stderr,
    )
    raise SystemExit(1)

folder = Path(__file__).resolve().parent

# Question 1: Create products.csv from sample product data and read it back.
products_file = folder / "products.csv"
products = pd.DataFrame(
    {
        "Product": ["Notebook", "Backpack", "Pen"],
        "Price": [4.50, 32.00, 1.25],
        "Stock": [120, 25, 300],
    }
)
products.to_csv(products_file, index=False)
products_from_csv = pd.read_csv(products_file)
print("Question 1: Products read from products.csv")
print(products_from_csv.to_string(index=False))

# Question 2: Select and display products that cost more than $5.
expensive_products = products_from_csv[products_from_csv["Price"] > 5]
print("\nQuestion 2: Products costing more than $5")
print(expensive_products.to_string(index=False))

# Question 3: Create marks.csv, read it, and calculate the average mark.
marks_file = folder / "marks.csv"
marks = pd.DataFrame(
    {
        "Student": ["Aisha", "Ben", "Carlos"],
        "Mark": [88, 76, 94],
    }
)
marks.to_csv(marks_file, index=False)
marks_from_csv = pd.read_csv(marks_file)
average_mark = marks_from_csv["Mark"].mean()
print(f"\nQuestion 3: The average mark is {average_mark:.1f}.")
