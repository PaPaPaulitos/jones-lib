from controllers import ReadFile, DirectoryScanner, FilterBreachedData



read_file = ReadFile('./files/fake_data.csv')
data = read_file.read()

filter_breached_data = FilterBreachedData()

filtered_data = filter_breached_data.filter_breached_data(data)

print(filtered_data)
