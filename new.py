import pandas as pd


def find_value(csv_file, target_value):
    df = pd.read_csv(csv_file)
    # try:
    #    location = df.where(df == target_value).stack().index[0]
    #    print(f"location: {location}")
    #    print(type(location))
    #    row_idx, col_idx = location
    #    print(f"row_idx: {row_idx}")
    #    print(type(row_idx))
    #    print(f"col_idx: {col_idx}")
    #    print(type(col_idx))
    #    return (row_idx + 1, col_idx + 1)  # Zeilen- und Spaltenindizes beginnen bei 1
    # except IndexError:
    #    return None
    print(df.where(df == target_value))


csv_file = "localisation.csv"  # Passe dies entsprechend deiner CSV-Datei an
target_value = "HELLOWORLD"  # Passe dies an den Wert an, den du suchen möchtest
find_value(csv_file=csv_file,target_value=target_value)