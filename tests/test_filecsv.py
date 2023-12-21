import os
import csv
from jones_lib.models import FileCSV  

def test_file_csv_read():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sample_csv_path = os.path.join(current_dir, 'resources', 'sample.csv')

    file_csv = FileCSV(sample_csv_path)

    data = []
    with open(sample_csv_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    assert data == file_csv.read()
