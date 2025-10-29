import pandas as pd

file_path = "ex2.csv"
def read_csv(filepath):
    data = pd.read_csv(filepath)
    return data

def clean_data(data):
    data = data.dropna()
    return data

def calculate_statistic(data, column):
    mean = data[column].mean()
    median = data[column].median()
    max = data[column].max()
    return f"statistics of column {column}, mean -> {mean} median -> {median} mode -> {max}"

def display_summary(stats: str):
    return stats

def main():
    df = read_csv(filepath=file_path)
    df = clean_data(data=df)
    stats = calculate_statistic(data=df, column="english")
    out = display_summary(stats)
    print(out)

if __name__ == "__main__":
    main()