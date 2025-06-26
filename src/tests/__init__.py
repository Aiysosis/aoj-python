from io import StringIO
import pytest
import importlib
from contextlib import redirect_stdout

def load_cases():
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

    with open('src/aoj/q001_maximum_profit/case.txt', 'r') as file:
        for line in map(lambda x: x.strip(), file):
            read_line(line)
        add_case()
    return cases

def pytest_generate_tests(metafunc):
    query = int(metafunc.config.getoption("--query"))
    if "algorithm" in metafunc.fixturenames:
        func = importlib.import_module('aoj.q001_maximum_profit').main
        metafunc.parametrize("algorithm", [func])
    if "case" in metafunc.fixturenames:
        metafunc.parametrize("case", load_cases())

def test_algorithm(case, algorithm, monkeypatch):
    input, expected_output = case
    monkeypatch.setattr('sys.stdin', StringIO(f"{input}\n"))
    tmp_out = StringIO()
    try:
        with redirect_stdout(tmp_out):
            algorithm()
    except Exception:
        pytest.fail("Error when executing algorithm")
    user_output = tmp_out.getvalue().strip()
    assert expected_output == user_output.strip()



def runTests():
    print("Input question id(leave empty to test all algorithms):")
    user_input = input()
    is_all = user_input.strip() == ""
    query_str = "-all" if is_all else f"--query={user_input}"
    pytest.main(["-vv", query_str, __file__])