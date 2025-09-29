import pandas as pd
import matplotlib.pyplot as plt

def analyze_sales_data():
    """
    This script performs data analysis on a sales CSV file.
    It loads the data, calculates total sales, aggregates the data,
    and generates two plots.
    """
    
    # --- Step 1: Load the CSV Dataset ---
    try:
        df = pd.read_csv('sales_data.csv')
        print("✅ CSV file loaded successfully.")
    except FileNotFoundError:
        print("❌ Error: 'sales_data.csv' not found. Make sure the file is in the same directory as the script.")
        return

    # --- Step 2: Initial Data Exploration ---
    print("\n--- Data Head ---")
    print(df.head())
    
    print("\n--- DataFrame Info ---")
    df.info()
    
    print(f"\n--- Data Shape ---")
    print(f"The DataFrame has {df.shape[0]} rows and {df.shape[1]} columns.")
    
    # --- Step 3: Data Preparation ---
    # Calculate the total sales for each transaction and add it as a new column
    df['TotalSales'] = df['UnitsSold'] * df['PricePerUnit']
    print("\n✅ 'TotalSales' column created.")
    print("\n--- Data Head with TotalSales ---")
    print(df.head())

    # --- Step 4: Data Analysis using groupby() ---
    # Calculate total sales per product
    product_sales = df.groupby('Product')['TotalSales'].sum().sort_values(ascending=False)
    print("\n--- Total Sales per Product ---")
    print(product_sales)

    # Calculate total units sold per category
    category_units = df.groupby('Category')['UnitsSold'].sum().sort_values(ascending=False)
    print("\n--- Total Units Sold per Category ---")
    print(category_units)

    # --- Step 5: Visualization 1: Bar Chart ---
    print("\n📊 Generating bar chart for total sales by product...")
    product_sales.plot(kind='bar', figsize=(10, 6), color='skyblue')
    
    # Add titles and labels for clarity
    plt.title('Total Sales by Product', fontsize=16)
    plt.xlabel('Product', fontsize=12)
    plt.ylabel('Total Sales ($)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout() # Adjust layout to make room for labels
    
    # Show the plot in a new window
    plt.show()

    # --- Step 6: Visualization 2: Pie Chart ---
    print("\n📊 Generating pie chart for units sold by category...")
    category_units.plot(kind='pie', figsize=(8, 8), autopct='%1.1f%%', startangle=140)

    plt.title('Percentage of Units Sold by Category', fontsize=16)
    plt.ylabel('') # Hide the y-label

    # Show the plot in a new window
    plt.show()

    print("\n🎉 Analysis complete.")


# --- Run the main analysis function ---
if __name__ == "__main__":
    analyze_sales_data()