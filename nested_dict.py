#Regular dict
import pandas as pd
category_df = pd.read_excel("excelfile.xlsv",sheet_name="Sheet1")

col_key = category_df.columns[0]       # Column A = keys
col_item = category_df.columns[1:]

def row_to_boolstr(row,column_flag):
    
    return ''.join(['1' if str(val).strip().lower() in ['y','Y'] else '0' for val in row [column_flag]]) 

bool_dict = {
    row[col_key]: row_to_boolstr(row,col_item)
    for _, row in category_df.iterrows()
}
part_property_df = pd.read_excel("excelfile.xlsv",sheet_name="Sheet2")

# 2. Extract key column and value columns
col_key = part_property_df.columns[1]       # Column A: 'Item'
col_item = part_property_df.columns[2:] # Columns B onward


# 3. Create the dictionary
part_property_dict = {
    row[col_key]: row_to_boolstr(row,col_item)
    for _, row in part_property_df.iterrows()
}
for item, bitstring in part_property_dict.items():
    print(f"{item} ➜ {bitstring}")
    # You can convert back to booleans or binary list:
    bools = [c == '1' for c in bitstring]



for item, bitstring in bool_dict.items():
    print(f"{item} ➜ {bitstring}")
    # You can convert back to booleans or binary list:
    bools = [c == '1' for c in bitstring]







############################################################################################


import pandas as pd

# Load the Excel file
df = pd.read_excel("your_file.xlsx")

# Define columns
category_col = "Category Type"
property_col = "Property"

# Extract all analysis type columns (everything else)
analysis_cols = df.columns.difference([category_col, property_col])

# Final result
nested_dict = {}

# Iterate by row
for _, row in df.iterrows():
    category = row[category_col]
    prop = row[property_col]

    for analysis in analysis_cols:
        flag = str(int(row[analysis]))  # convert to string '1' or '0'

        cat_key = f"{category}|{flag}"
        prop_key = f"{prop}|{flag}"

        # Initialize analysis type if not yet present
        if analysis not in nested_dict:
            nested_dict[analysis] = {}

        # Initialize category if not yet present
        if cat_key not in nested_dict[analysis]:
            nested_dict[analysis][cat_key] = {}

        # Add property
        nested_dict[analysis][cat_key][prop_key] = {}
        

#################################################################

import pandas as pd

# Load your Excel
df = pd.read_excel("your_file.xlsx")

# Define your key columns
property_col = "Property"
analysis_col = "Analysis"
category_cols = df.columns.difference([property_col, analysis_col])

# Final output dict
nested_dict = {}

# Iterate row-by-row
for _, row in df.iterrows():
    analysis = row[analysis_col]
    prop = row[property_col]

    # Create entry if analysis not yet in the dict
    if analysis not in nested_dict:
        nested_dict[analysis] = {}

    # Loop over category columns
    for category in category_cols:
        cat_flag = str(int(row[category]))
        prop_flag = cat_flag  # assumed same logic for prop flag

        cat_key = f"{category}|{cat_flag}"
        prop_key = f"{prop}|{prop_flag}"

        if cat_key not in nested_dict[analysis]:
            nested_dict[analysis][cat_key] = {}

        nested_dict[analysis][cat_key][prop_key] = {}
        
        
        
#############################################################################################
import pandas as pd

# Load Excel
df = pd.read_excel("your_file.xlsx")

# Define columns
category_col = "Category Type"
property_col = "Property"
analysis_cols = df.columns.difference([category_col, property_col])

# Final output dictionary
nested_dict = {}

# Normalize "Y" / "N" to 1 / 0
def normalize_flag(val):
    return 1 if str(val).strip().upper() == "Y" else 0

# Build structure
for _, row in df.iterrows():
    category = row[category_col]
    prop = row[property_col]

    for analysis in analysis_cols:
        flag = normalize_flag(row[analysis])

        # Init analysis
        if analysis not in nested_dict:
            nested_dict[analysis] = {}

        # Init category
        if category not in nested_dict[analysis]:
            nested_dict[analysis][category] = {"Flag": flag}
        else:
            # Ensure flag is 1 if *any* property under this category has a 1
            nested_dict[analysis][category]["Flag"] = max(nested_dict[analysis][category]["Flag"], flag)

        # Set property flag
        nested_dict[analysis][category][prop] = flag
        
import json
# Pretty-print the nested dictionary
print(json.dumps(nested_dict, indent=2))


for analysis, categories in nested_dict.items():
    print(f"\n[Analysis: {analysis}]")

    for category, props in categories.items():
        if props.get("Required") != '1':
            continue  # Skip disabled categories

        print(f"  [Category: {category}]")

        for prop, flag in props.items():
            if prop == "Required":
                continue  # Skip the 'Flag' key itself

            if flag == 1:
                print(f"    ✔ Property: {prop}")
            else:
                print(f"    ✘ Property: {prop} (disabled)")