# conftest.py

def pytest_addoption(parser):
    parser.addoption("--api_key", action="store", default="aaa")