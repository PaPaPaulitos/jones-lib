import os
import json

from jones_lib.models import FileJSON

def test_file_json_read():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sample_json_path = os.path.join(current_dir, 'resources', 'sample.json')

    file_json = FileJSON(sample_json_path)

    with open(sample_json_path, mode='r', encoding='utf-8') as file:
        data = json.load(file)

    assert data == file_json.read()