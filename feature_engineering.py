import pandas as pd
import numpy as np

def feature_engineering():
    # Load enriched product data and order products prior data
    products = pd.read_csv('enriched_products.csv')
    order_products_prior = pd.read_csv('order_products__prior.csv')

    # Merge order products with product info
    merged = pd.merge(order_products_prior, products, on='product_id', how='left')

    # Simulate some features inspired by the paper
    # For example: review length (simulated), sentiment score (simulated), verified purchase (simulated)
    np.random.seed(42)
    merged['review_length'] = np.random.randint(10, 500, size=len(merged))
    merged['sentiment_score'] = np.random.uniform(-1, 1, size=len(merged))
    merged['verified_purchase'] = np.random.choice([0, 1], size=len(merged))

    # Create a feature set for demonstration
    features = merged[['product_id', 'review_length', 'sentiment_score', 'verified_purchase', 'reordered']]

    # Save features to CSV
    features.to_csv('feature_set.csv', index=False)
    print("Feature engineering completed and saved to 'feature_set.csv'")

if __name__ == "__main__":
    feature_engineering()
