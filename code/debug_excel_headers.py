import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_PATH = os.path.join(BASE_DIR, "Documents for training", "Training plan", "Training-plan-template.xlsx")

try:
    print(f"Reading: {EXCEL_PATH}")
    df = pd.read_excel(EXCEL_PATH, sheet_name="ELP")
    print("\nColumns found:")
    for col in df.columns:
        print(f"'{col}'")
        
    print("\nFirst record (raw):")
    print(df.iloc[0].to_dict())
except Exception as e:
    print(f"Error: {e}")
