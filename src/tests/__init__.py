from io import StringIO
import logging
from os import listdir, path
import pytest
import importlib
from contextlib import redirect_stdout
import re

from utils.path import AOJ

def load_cases(q_name: str):
    cases = []
    input_lines = []
    output_lines = []
    is_input = True

    def add_case():
        new_case = ('\n'.join(input_lines), '\n'.join(output_lines))
        cases.append(new_case)
        input_lines.clear()
        output_lines.clear()

    def read_line(line: str):
        nonlocal is_input
        match line:
            case '<<':
                if not is_input:
                    add_case()
                is_input = True
            case '>>':
                is_input = False
            case _ if is_input:
                input_lines.append(line)
            case _:
                output_lines.append(line)

    with open(AOJ / q_name / 'case.txt', 'r') as file:
        for line in map(lambda x: x.strip(), file):
            read_line(line)
        add_case()
    return cases

def pytest_generate_tests(metafunc):
    query = metafunc.config.getoption("--query")
    if "algorithm" in metafunc.fixturenames:
        func = importlib.import_module(f'aoj.{query}').main
        metafunc.parametrize("algorithm", [func])
    if "case" in metafunc.fixturenames:
        metafunc.parametrize("case", load_cases(query))

def test_algorithm(case, algorithm, monkeypatch):
    input, expected_output = case
    monkeypatch.setattr('sys.stdin', StringIO(f"{input}\n"))
    tmp_out = StringIO()
    try:
        with redirect_stdout(tmp_out):
            algorithm()
    except Exception as e:
        pytest.fail("Error when executing algorithm")
        logging.exception(e)
    user_output = tmp_out.getvalue().strip()
    assert expected_output == user_output.strip()

def search_algorithm(query: str):
    file_list = listdir(AOJ)
    for file in file_list:
        if path.isdir(AOJ / file) and re.match(r'^q[0-9]{3}', file):
            if query in file:
                return file

def run_tests():
    print("Input question id:")
    query_str = input()
    name = search_algorithm(query_str)
    if name == None:
        print("No question matches input id")
        return
    else:
        print(f"Testing algorithm {name}")
        query_str = f"--query={name}"

    pytest.main(["-vvl", query_str, __file__])