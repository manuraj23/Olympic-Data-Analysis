import pandas as pd
import os, sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# Load the CSV file
df = pd.read_csv(resource_path('odi_Batting_Card.csv'))

def preprocess(df):
    # Create dummy variables for the 'wicketType' column and concatenate them to the DataFrame
    df = pd.concat([df, pd.get_dummies(df['isOut'])], axis=1)
    return df

# Preprocess the DataFrame
df = preprocess(df)

# Save the processed DataFrame to an Excel file
output_file = "output_file.xlsx"
df.to_excel(output_file, index=False)

# Print a confirmation message with the correct file name
print("Merged data saved to", output_file)


# def merge_excel_files(file1, file2, output_file):
#     # Read the Excel files
#     df1 = pd.read_excel(file1)
#     df2 = pd.read_excel(file2)
    
#     # Merge the DataFrames based on the "player_id" column
#     merged_df = pd.merge(df1, df2, on='player_id', how='inner')
    
#     # Write the merged data to a new Excel file
#     merged_df.to_excel(output_file, index=False)
#     print("Merged data saved to", output_file)

# # Example usage
# merge_excel_files("file1.xlsx", "file2.xlsx", "merged_file.xlsx")
