import pandas as pd

def preprocess_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Convert date columns
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    df['Delivery_Date'] = pd.to_datetime(df['Delivery_Date'])

    # Create new feature: delivery time
    df['Delivery_Days'] = (df['Delivery_Date'] - df['Order_Date']).dt.days

    # Handle missing values
    df.fillna(method='ffill', inplace=True)

    # Save cleaned data
    df.to_csv(output_path, index=False)
    print("✅ Data preprocessing completed")

if __name__ == "__main__":
    preprocess_data(
        "data/raw/supply_chain_data.csv",
        "data/processed/cleaned_data.csv"
    )
