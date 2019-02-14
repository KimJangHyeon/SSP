import os, re

directory = os.listdir('./TEST')
os.chdir('./TEST')

for file in directory:
    open_file = open(file, 'r', encoding='UTF8')
    read_file = open_file.read()
    print(read_file)
    read_file = read_file.replace('\t', ' ')
    open_file.close()

    open_file = open(file, 'w', encoding='UTF8')
    open_file.write(read_file)
    open_file.close()
    print('=============')