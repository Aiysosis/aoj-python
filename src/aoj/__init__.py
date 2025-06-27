from os import listdir, mkdir
import re
from shutil import copyfile
from utils.path import AOJ, TEMPLATE

def new_algorithm():
    print("Input algorithm name:")
    name = input().strip()
    if re.search(r'[^\s0-9a-zA-Z]+', name):
        print("Invalid name")
        return
    name = re.sub(r'\s+', '_', name).lower()
    def is_algorithm(s):
        return re.match(r'^q[0-9]{3}' ,s) != None
    file_list = list(filter(is_algorithm, listdir(AOJ)))
    new_file_name = f"q{str(len(file_list) + 1).rjust(3, '0')}_{name}"
    print(f"Generating file {new_file_name}")
    new_dir_path = AOJ / new_file_name
    mkdir(new_dir_path)
    copyfile(TEMPLATE / 'template.py', new_dir_path / '__init__.py')
    copyfile(TEMPLATE / 'template.txt', new_dir_path / 'case.txt')
    print("Done!")
