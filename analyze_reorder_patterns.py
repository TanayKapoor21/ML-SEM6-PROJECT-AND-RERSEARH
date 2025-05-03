import pandas as pd

def analyze_reorder_patterns():
    # Load enriched product data and order products prior data
    products = pd.read_csv('enriched_products.csv')
    order_products_prior = pd.read_csv('order_products__prior.csv')

    # Merge order products with product info
    merged = pd.merge(order_products_prior, products, left_on='product_id', right_on='product_id', how='left')

    # Calculate reorder rate per product
    reorder_rate_product = merged.groupby('product_id')['reordered'].mean().reset_index()
    reorder_rate_product = pd.merge(reorder_rate_product, products[['product_id', 'product_name']], on='product_id', how='left')

    # Calculate reorder rate per aisle
    reorder_rate_aisle = merged.groupby('aisle_name')['reordered'].mean().reset_index()

    # Calculate reorder rate per department
    reorder_rate_department = merged.groupby('department_name')['reordered'].mean().reset_index()

    # Save results to CSV files
    reorder_rate_product.to_csv('reorder_rate_per_product.csv', index=False)
    reorder_rate_aisle.to_csv('reorder_rate_per_aisle.csv', index=False)
    reorder_rate_department.to_csv('reorder_rate_per_department.csv', index=False)

    print("Reorder rate analysis saved to CSV files.")

if __name__ == "__main__":
    analyze_reorder_patterns()
