def pytest_addoption(parser):
    parser.addoption("--query", action="store", help="search an algorithm and perform test")