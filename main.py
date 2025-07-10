import pandas as pd
import src.data_cleaning as dc
import src.eda as eda
import src.visualization as viz

# Load data
df = pd.read_csv("data/googleplaystore.csv")

# Clean data
df_clean = dc.clean_data(df)

# Run EDA
eda.run_eda(df_clean)

# Visualize data
viz.plot_all(df_clean)