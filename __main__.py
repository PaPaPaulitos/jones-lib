from controllers import BreachedData

PATH = './files/'

bd = BreachedData(PATH)

file_list = bd.get_files_list()

print(file_list)

for file in file_list:
    data = bd.read(PATH + file)
    filtered_data = bd.filter(data)

    in_breached_data = bd.search(filtered_data,'paulitos','pauloricardomrs2002@gmail.com')

    if in_breached_data:
        print('Your data was breached')




