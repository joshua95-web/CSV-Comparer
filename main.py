import csv

def read_csv(file_path, encoding='utf-8'):
    with open(file_path, mode='r', newline='', encoding=encoding, errors='replace') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def find_differences(file1, file2):
    content1 = read_csv(file1)
    content2 = read_csv(file2)
    
    # Convert list of dicts to set of tuples for easier comparison
    set1 = {tuple(sorted(item.items())) for item in content1}
    set2 = {tuple(sorted(item.items())) for item in content2}
    
    only_in_file1 = set1 - set2
    only_in_file2 = set2 - set1
    
    return only_in_file1, only_in_file2

def print_differences(only_in_file1, only_in_file2):
    if only_in_file1:
        print("Rows only in file 1:")
        for row in only_in_file1:
            print(dict(row))
    else:
        print("No unique rows in file 1.")
    
    if only_in_file2:
        print("Rows only in file 2:")
        for row in only_in_file2:
            print(dict(row))
    else:
        print("No unique rows in file 2.")

# Paths to your CSV files
file1 = 'one_that_worked.csv'
file2 = "didn't_work.csv"

# Find and print differences
only_in_file1, only_in_file2 = find_differences(file1, file2)
print_differences(only_in_file1, only_in_file2)