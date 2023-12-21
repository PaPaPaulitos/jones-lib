from controllers import BreachedData

PATH = './files/'

bd = BreachedData(PATH)

files,file_list = bd.get_files_list()

print(files)
print(file_list)


for file in files:
    data = bd.read(PATH + file)
    filtered_data = bd.filter(data)

    in_breached_data = bd.search(filtered_data,'paulitos','pauloricardomrs2002@gmail.com')

    if in_breached_data:
        for f in file_list:
            if file in f.keys():
                print(f'Your data was breached in {f[file]}')
        





