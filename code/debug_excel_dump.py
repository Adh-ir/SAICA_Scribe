import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_PATH = os.path.join(BASE_DIR, "Documents for training", "Training plan", "Training-plan-template.xlsx")

try:
    df = pd.read_excel(EXCEL_PATH, sheet_name="ELP")
    # Drop rows where 'Competency' is null to bypass header junk
    df_clean = df.dropna(subset=['Competency'])
    
    print(f"Total Rows: {len(df)}")
    print(f"Clean Rows: {len(df_clean)}")
    
    print("\n--- Sample Record ---")
    if not df_clean.empty:
        rec = df_clean.iloc[0].to_dict()
        for k, v in rec.items():
            print(f"{k}: {v}")
    else:
        print("No clean records found.")
        
except Exception as e:
    print(f"Error: {e}")
