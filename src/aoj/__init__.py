import importlib
from aoj.utils.test import startTest
import os

def runTest():
    print("Input Question id: ")
    question_id = input()
    with os.scandir('./src/aoj') as entries:
        dir_names = [entry.name for entry in entries if entry.is_dir()]
        matched = False
        for name in dir_names:
            if question_id in name:
                matched = True
                print(f"Running test of {name}")
                q_module = importlib.import_module(f"aoj.{name}")
                case_path = f"./src/aoj/{name}/case.txt"
                startTest(case_path, q_module.main)
        if not matched:
            print('No question matched this id')

def createQuestion():
    print("Input Question name: ")
    question_name = input()