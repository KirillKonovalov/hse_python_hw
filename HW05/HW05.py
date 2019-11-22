import os
import re

def folders(folder="."):
    all_folders = []
    for root, dirs, files in os.walk(folder):
        for d in dirs:
            all_folders.append(d)
    return all_folders
    
def files(folder="."):
    all_files = []
    for root, dirs, files in os.walk(folder):
        for f in files:
            all_files.append(f)
    return all_files
    
def number_of_folders(folders):
    dirs_with_digits = []
    dirs_with_cyrillics = []
    
    for folder in folders:
        if re.findall('\d', folder):
            dirs_with_digits.append(folder)
        if not re.findall('\d', folder):
            if re.findall('[А-я]+', folder):
                if not re.findall('[A-z]+', folder):
                    dirs_with_cyrillics.append(folder)
                    
    print('Количество папок с цифрами в названии: ', len(dirs_with_digits), '\nКоличество папок только с кириллическими символами: ', len(dirs_with_cyrillics))

def number_of_files(files):
    files_without_digits = []
    files_with_latins = []
    
    for file in files:
        if not re.findall('\d+', file):
            files_without_digits.append(file)
        if not re.findall('\d', file):
            if len(file) == len(file.encode()):
                files_with_latins.append(file)
    
    print('Количество файлов без цифр в названии: ', len(files_without_digits), '\nКоличество файлов только с латинскими символами: ', len(files_with_latins))

def unique_names(folders, files):
    unique_f_names = []
    
    for folder in set(folders):
        unique_f_names.append(folder)
    for file in set(files):
        unique_f_names.append(file)
    
    print('Cписок уникальных названий файлов и папок: ', (set(unique_f_names)))

def main():  
    print(number_of_folders(folders()))
    print(number_of_files(files()))
    print(unique_names(folders(), files()))

if __name__ == '__main__':
    main()
