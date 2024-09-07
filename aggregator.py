import pandas as pd
import os

def load_data(directory_path):
    csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]
    dataframes = []

    for file in csv_files:
        file_path = os.path.join(directory_path, file)
        df = pd.read_csv(file_path)
        dataframes.append(df)
        print(f"loaded {file} with {len(df)} rows!!")

    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df

def aggregate_data(df, group_by_column, agg_column, aggregation_func = 'sum'):

    aggregated_df = df.groupby(group_by_column)[agg_column].agg(aggregation_func).reset_index()
    return aggregated_df

def save_data(df, output_file):

    df.to_csv(output_file, index = False)
    print("Aggregated data saved to " + output_file)
    
def main():

    directory_path = "C:\\Users\\poude\\OneDrive\\Desktop\\Python files\\Data_aggregator\\path\\"

    combined_df = load_data(directory_path)

    aggregated_df = aggregate_data(combined_df, group_by_column = 'Product', agg_column = 'Sales', aggregation_func = 'sum')
    print("Agggregated Data: ")
    print(aggregated_df.head())

    output_file = 'Aggregated_data.csv'
    save_data(aggregated_df, output_file)

if __name__ == "__main__":
    main()
