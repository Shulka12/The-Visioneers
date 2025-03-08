import csv
import pandas as pd

def read_csv_file(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]
    
    for row in data:
        print(row)
    
    def read_csv_file(file_path):
        with open(file_path, mode='r') as file:
            data = pd.read_csv(file_path)
            data = [row for row in csv_reader]
        
        for row in data:
            print(row)
        
        return data
    if __name__ == "__main__":
        file_path = 'path_to_your_csv_file.csv'
        read_csv_file(file_path)