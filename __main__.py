from controllers import ReadFile, DirectoryScanner



read_file = ReadFile('./files/fake_data.csv')
data = read_file.read()
print(data)