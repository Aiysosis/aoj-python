def pytest_addoption(parser):
    parser.addoption("--all", action="store_true", help="run all tests")
    parser.addoption("--query", action="store", help="select an algorithm for testing")