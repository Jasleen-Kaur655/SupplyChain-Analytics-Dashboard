from src.data_preprocessing import preprocess_data
from src.analysis import analyze_data
from src.visualization import create_visualizations

RAW_DATA = "data/raw/supply_chain_data.csv"
CLEAN_DATA = "data/processed/cleaned_data.csv"

preprocess_data(RAW_DATA, CLEAN_DATA)
analyze_data(CLEAN_DATA)
create_visualizations(CLEAN_DATA)
