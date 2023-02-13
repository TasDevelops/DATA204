def open_file(file_name):
    
    try:
        file = open('file_name', 'r')
        file_lines = file.readlines()
        for line in file_lines:
            print(line.rstrip('\n'))
    except FileNotFoundError as errmsg:
        print('File cant be found', errmsg)
        raise