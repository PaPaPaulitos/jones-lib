from controllers import ReadFile, DirectoryScanner


scanner = DirectoryScanner('./files')
files = scanner.get_files_list()

print(files)

for file in files:
    read_file = ReadFile('./files/' + file)
    data = read_file.read()
    print(data)