import pandas as pd

def clear_excel_file():
    """
    Clear all data from training_data.xlsx while keeping the headers
    """
    excel_path = "training_data.xlsx"
    
    # Create empty DataFrame with the same columns
    df = pd.DataFrame(columns=[
        'Run_ID',
        'Episode',
        'Episode_Reward',
        'Episode_Length',
        'Epsilon',
        'TD_Error',
        'Goal_Reached',
        'Steps_to_Goal',
        'Saved_Model',
        'Timestamp',
        'Cumulative_Reward'
    ])
    
    # Save the empty DataFrame
    df.to_excel(excel_path, index=False)
    print(f"All data cleared from {excel_path}. Only headers remain.")

if __name__ == "__main__":
    clear_excel_file()
