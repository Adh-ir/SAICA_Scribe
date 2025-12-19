import pandas as pd
import logging

logger = logging.getLogger(__name__)

def load_training_plan(file_path):
    """
    Reads the 'ELP' tab from the Training Plan Excel file.
    
    Args:
        file_path (str): Absolute path to the .xlsx file.
        
    Returns:
        list: A list of dictionaries representing the competencies/tasks.
    """
    try:
        logger.info(f"Loading training plan from: {file_path}")
        # Read the "ELP" sheet
        # Note: We need to verify if the sheet name is exactly "ELP" or has spaces.
        df = pd.read_excel(file_path, sheet_name="ELP")
        
        # Clean and Map
        clean_records = []
        last_valid_name_4 = None
        last_valid_name_2 = None
        
        for _, row in df.iterrows():
            # Update running valid names (Forward Fill)
            curr_name_4 = row.get('Unnamed: 4')
            if not pd.isna(curr_name_4) and str(curr_name_4).strip().lower() != 'nan':
                 last_valid_name_4 = str(curr_name_4).strip()
                 
            curr_name_2 = row.get('Unnamed: 2')
            if not pd.isna(curr_name_2) and str(curr_name_2).strip().lower() != 'nan':
                 last_valid_name_2 = str(curr_name_2).strip()

            # Skip if critical fields are empty (but after updating state!)
            if pd.isna(row.get('Competency')) and pd.isna(row.get('Learning outcome')):
                continue
                
            # Construct standard keys
            # Code: Combine ID/Competency with Outcome (e.g. "1.1 (a)")
            comp_id = str(row.get('Id') or row.get('Competency') or '').replace('.0', '').strip()
            outcome = str(row.get('Learning outcome') or '').strip()
            
            code = f"{comp_id}{outcome}"
            
            # Name Logic: Use current specific name, else fallback to last specific, else group
            name = last_valid_name_4
            if not name: name = last_valid_name_2
            if not name: name = f"Competency {code}" 

            desc = str(row.get('Unnamed: 6') or '').strip()
            if desc.lower() == 'nan': desc = ""
            
            clean_records.append({
                "competency_code": code,
                "competency_name": name,
                "behavioral_indicators": desc,
                "original_row": row.to_dict() 
            })
            
        logger.info(f"Successfully loaded {len(clean_records)} clean records from ELP tab.")
        return clean_records

    except Exception as e:
        logger.error(f"Failed to load training plan: {e}")
        return []
