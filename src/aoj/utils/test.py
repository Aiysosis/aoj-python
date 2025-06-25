import sys
import unittest
from io import StringIO
from contextlib import redirect_stdout
import logging
from typing import Callable

class TestInOJStyle(unittest.TestCase):
    @classmethod
    def init_test(cls, caseFile: str, algorithm: Callable[[], None]):
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

        with open(caseFile, 'r') as file:
            for line in map(lambda x: x.strip(), file):
                read_line(line)
            add_case()
        print(cases)
        cls.cases = cases
        cls.algorithm = staticmethod(algorithm)

    def test_main(self):
        if not self.cases:
            self.fail("No test cases loaded! Check file path and format.")
        for i, (input, output) in enumerate(self.cases):
            with self.subTest():
                sys.stdin = StringIO(input)
                tmp_out = StringIO()
                try:
                    with redirect_stdout(tmp_out):
                        self.algorithm()
                except Exception as e:
                    logging.exception(e)
                user_output = tmp_out.getvalue().strip()
                #recover stdin
                sys.stdin = sys.__stdin__
                self.assertEqual(output, user_output, f"'Case #{i+1} Failed")
                print(f"✓ Case #{i+1} Passed!")

def startTest(case_path: str, algorithm: Callable[[], None]):
    TestInOJStyle.init_test(case_path, algorithm)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestInOJStyle)
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)