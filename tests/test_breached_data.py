import os

from jones_lib.controllers import BreachedData
from faker import Faker

fake = Faker()

current_dir = os.path.dirname(os.path.abspath(__file__))

EXTENSION = ['csv','xlsx','json']

def test_get_files_list():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    PATH = os.path.join(current_dir, 'resources')
    bd_instance = BreachedData(PATH)
    files_list = bd_instance.get_files_list()
    assert isinstance(files_list, tuple), "get_files_list should return a tuple of lists"
    assert all(isinstance(lst, list) for lst in files_list), "All items in the tuple should be lists"

def test_read():
    number = fake.random_int(min=0, max=2)
    file_name = f'\\sample.{EXTENSION[number]}'
    PATH = os.path.join(current_dir, 'resources')
    bd_instance = BreachedData(PATH)

    return_value = bd_instance.read(file_name)

    assert isinstance(return_value, list), "read should return a list"

    for item in return_value:
        assert isinstance(item, dict), "Each item in the list should be a dictionary"
        assert all(isinstance(key, str) for key in item.keys()), "All keys should be strings"

def test_filter():
    number = fake.random_int(min=0, max=2)
    file_name = f'\\sample.{EXTENSION[number]}'
    PATH = os.path.join(current_dir, 'resources')
    bd_instance = BreachedData(PATH)

    normal_dict = bd_instance.read(file_name)

    filter_dict = bd_instance.filter(normal_dict)

    assert isinstance(filter_dict, list), "filter_dict should be a list"

    for item in filter_dict:
        assert isinstance(item, dict), "Each item in filter_dict should be a dictionary"

        assert set(item.keys()) == {'email', 'username'}, "Each item should only have 'email' and 'username' as keys"


def test_search():
    number = fake.random_int(min=0, max=2)
    file_name = f'\\sample.{EXTENSION[number]}'
    PATH = os.path.join(current_dir, 'resources')
    bd_instance = BreachedData(PATH)

    fake_email = fake.email()

    fake_username = fake.user_name()

    normal_dict = bd_instance.read(file_name)

    filter_dict = bd_instance.filter(normal_dict)

    search_dict = bd_instance.search(filter_dict,username=fake_username,email=fake_email)

    assert isinstance(search_dict, bool), "search_dict should be a list"


def test_scan():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    PATH = os.path.join(current_dir, 'resources')
    PATH = PATH + '\\'
    bd_instance = BreachedData(PATH)

    fake_email = fake.email()

    fake_username = fake.user_name()

    search_dict = bd_instance.scan(username=fake_username,email=fake_email)

    assert isinstance(search_dict, list), "scan should return a dictionary"







    

