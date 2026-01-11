import pandas as pd
import matplotlib.pyplot as plt

def create_visualizations(file_path):
    df = pd.read_csv(file_path)

    # Group data by Region and calculate average delivery days
    region_delivery = df.groupby('Region')['Delivery_Days'].mean()

    # Plot bar chart
    region_delivery.plot(kind='bar', color='skyblue')
    plt.title("Average Delivery Time by Region")
    plt.xlabel("Region")
    plt.ylabel("Delivery Days")
    plt.tight_layout()

    # ✅ Save chart as PNG before showing
    plt.savefig("dashboard_chart.png", dpi=150)
    
    # Show chart
    plt.show()

if __name__ == "__main__":
    create_visualizations("data/processed/cleaned_data.csv")
