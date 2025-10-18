import pandas as pd
from fuzzywuzzy import fuzz, process

# First, defining functions
# Load data and headers 
def load_data():
    
    df = pd.read_csv("mn.csv", dtype=str)
    hdr_df = pd.read_csv("mn_headers.csv", dtype=str, keep_default_na=False)

    # Determine acronym and description columns
    acr_col = hdr_df.columns[0]
    desc_col = hdr_df.columns[1] if len(hdr_df.columns) > 1 else hdr_df.columns[0]

    # Build mapping dictionary
    header_map = pd.Series(hdr_df[desc_col].values, index=hdr_df[acr_col]).to_dict()
    return df, header_map


# Map headers where possible
def map_headers(df, header_map):
    
   # Replace acronyms with readable headers where available, returns df and list of unmatched columns
    matched_cols = {col: header_map[col] for col in df.columns if col in header_map}
    unmatched_cols = [col for col in df.columns if col not in header_map]

    # Rename columns where mapping exists
    df = df.rename(columns=matched_cols)
    return df, unmatched_cols


# Remove spaces from strings 
def clean_strings(df):
    return df.applymap(lambda x: x.strip() if isinstance(x, str) else x)


# Normalize yes/no columns 
def normalize_yes_no(df, yes_no_cols):
    for col in yes_no_cols:
        if col in df.columns:
            df[col] = df[col].str.title()
    return df


# Convert numeric columns 
def convert_numeric(df, numeric_cols):
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


# Handle missing values 
def handle_na(df, drop_subset=None, fill_dict=None):
    if drop_subset:
        df = df.dropna(subset=drop_subset)
    if fill_dict:
        for col, val in fill_dict.items():
            if col in df.columns:
                df[col] = df[col].fillna(val)
    return df


# Remove duplicates
def remove_duplicates(df):
    return df.drop_duplicates()


# Inspect unmatched columns - printing first 5 rows
def inspect_unmatched_columns(df, unmatched_cols):
    if unmatched_cols:
        print("\nUnmatched columns detected:")
        for col in unmatched_cols:
            unique_vals = df[col].dropna().unique()[:5]
            print(f"  {col}: {list(unique_vals)}")
    else:
        print("\nNo unmatched columns detected.")


# Fuzzy match strings 
def best_match(query, choices):
    return process.extractOne(query, choices)


# Main function
def main():
    # Load data and header mapping
    df, header_map = load_data()
    print(f"Data loaded. Total columns: {len(df.columns)}")

    # Map headers and detect unmatched columns
    df, unmatched_cols = map_headers(df, header_map)
    print(f"Matched columns: {len(df.columns) - len(unmatched_cols)}")
    print(f"Unmatched columns: {len(unmatched_cols)}")

    # Inspect unmatched columns (First 5 unique values)
    inspect_unmatched_columns(df, unmatched_cols)

    # Clean strings
    df = clean_strings(df)

    # Example normalization for yes/no columns
    df = normalize_yes_no(df, yes_no_cols=['Ever Smoked'])  # update as needed

    # Convert numeric columns
    numeric_cols = ['Age', 'Survey Weight', 'Score_U', 'Index5_U', 'Score_R', 'Index5_R']
    df = convert_numeric(df, numeric_cols)

    # Handle missing values
    df = handle_na(df, drop_subset=['Age'], fill_dict={'Survey Weight': 0})

    # Remove duplicates
    df = remove_duplicates(df)

    # Save intermediate cleaned data
    df.to_csv("mn_clean_intermediate.csv", index=False)
    print("\nIntermediate cleaned CSV saved as mn_clean_intermediate.csv")


if __name__ == "__main__":
    main()
