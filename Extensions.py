File_extensions = ['.gif', '.jpg', 'jpeg', '.png', '.pdf', '.txt', '.zip']
File_types = ['Image/gif', 'Image/Jpg', 'Image/jpeg', 'Image/png', 'Document/pdf', 'Document/txt', 'Archive/zip']
File = input('What is the file name? (Include extension) ')

text = File[-4:]

if text in File_extensions:
    position = File_extensions.index(text)
    print(f'{File_types[position]}')
else:
    print('application/octet-stream')









