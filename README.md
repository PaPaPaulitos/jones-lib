<p align=center>
  <br>
  <img width="70%" height="70%" src="./Images/Jones-lib.svg">
  <br>
  <span>Explore breached data</span>
  <br>
</p>

## Installation

```bash
# Installing using pip
$ pip install jones-lib
```

## Usage

- Import `BreachedData` object

```python
from jones_lib import BreachedData
```

- When you instantiate a `BreachedData` object, you need to pass a `PATH` to your breached data.

```python
PATH = './files/'

bd = BreachedData(PATH)
```

### Jones functions

- **get_files_list()**

```python
    files,file_list = bd.get_files_list()
```

This function will return 2 lists:

- files: Filenames in the PATH

- file_list: A list of dictionaries where the key is the filename and the value is the name of the website.

<br>

- **read()**

```python
    data = bd.read(PATH + file)
```

This function will receive a PATH + filename and will return a dictionary of your data.

- **filter()**

```python
    filtered_data = bd.filter(data)
```

This function takes a dictionary (usually the **read** function dictionary) and filters it so that it only has the `username` and `email` fields.

- **search()**

```python
in_breached_data = bd.search(filtered_data,username=USERNAME,email=EMAIL)
```
This function takes a dictionary (typically you want to send the dictionary from the **filter** function) and you will pass the `username` and `email` of your target, returning a boolean indicating whether or not it is in the leaked data.