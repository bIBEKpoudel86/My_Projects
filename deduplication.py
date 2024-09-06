import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    print("Original data: ")
    print(df.head())
    return df

def remove_duplicates(df,subset_columns):
    deduplicated_df = df.drop_duplicates(subset = subset_columns)
    print("Data after Deduplicating:")
    print(deduplicated_df.head())
    return deduplicated_df

def save_data(df, output_file):
    df.to_csv(output_file, index = False)
    print("Data are saved into " + output_file)


def main():
    input_file = "C:\\Users\\poude\\OneDrive\Desktop\\Python files\\Data_Deduplication\\data.csv"
    output_file = "deduplicated_data.csv"

    df = load_data(input_file)

    duplicated_df = remove_duplicates(df, subset_columns = ["Name", "Email"])

    save_data(duplicated_df, output_file)


if __name__ == '__main__':
    main()
