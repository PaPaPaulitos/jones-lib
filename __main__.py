from controllers import ReadFile

read_file = ReadFile('new_fake_data.xlsx')
data = read_file.read()
print(data)