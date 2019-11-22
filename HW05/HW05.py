import os
import re

all_folders = []
all_files = []

dirs_with_digits = []
files_without_digits = []
dirs_with_cyrillics = []
files_with_latins = []

for root, dirs, files in os.walk("."):
    for d in dirs:
        all_folders.append(d)
    for f in files:
        all_files.append(f)
        
for folder in all_folders:
    if re.findall('\d', folder):
        dirs_with_digits.append(folder)
    if not re.findall('\d', folder):
        if re.findall('[А-я]+', folder):
            if not re.findall('[A-z]+', folder):
                dirs_with_cyrillics.append(folder)

for file in all_files:
    if not re.findall('\d+', file):
        files_without_digits.append(file)
    if not re.findall('\d', file):
        if len(file) == len(file.encode()):
            files_with_latins.append(file)
    
print('Количество папок с цифрами в названии:', len(dirs_with_digits))
print('Количество файлов без цифр в названии:', len(files_without_digits))
print('Количество папок только с кириллическими символами:', len(dirs_with_cyrillics))
print('Количество файлов только с латинскими символами:', len(files_with_latins))

print('\nСписок уникальных названий папок:', [str(f) for f in set(all_folders)])
print('\nСписок уникальных названий файлов:', [str(f) for f in set(all_files)])
