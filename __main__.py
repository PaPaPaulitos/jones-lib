from controllers import ReadFile, DirectoryScanner, FilterBreachedData



read_file = ReadFile('./files/fake_data.csv')
data = read_file.read()

filter_breached_data = FilterBreachedData()

filtered_data = filter_breached_data.filter_breached_data(data)

in_breached_data = filter_breached_data.search_in_filter_data(filtered_data,'paulitos','pauloricardomrs2002@gmail.com')

if in_breached_data:
    print('Your data was breached')