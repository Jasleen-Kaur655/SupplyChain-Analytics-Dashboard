import pandas as pd

def analyze_data(file_path):
    df = pd.read_csv(file_path)

    avg_delivery = df['Delivery_Days'].mean()
    avg_cost = df['Shipping_Cost'].mean()
    delay_rate = (df['Delivery_Status'] == 'Delayed').mean() * 100

    print("📊 Supply Chain Analysis")
    print(f"Average Delivery Time: {avg_delivery:.2f} days")
    print(f"Average Shipping Cost: {avg_cost:.2f}")
    print(f"Delay Rate: {delay_rate:.2f}%")

    return df

if __name__ == "__main__":
    analyze_data("data/processed/cleaned_data.csv")
