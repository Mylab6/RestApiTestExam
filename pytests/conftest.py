# conftest.py

def pytest_addoption(parser):
    parser.addoption("--api_key", action="store", default="No_API_Key")
    parser.addoption("--mapid", action="store", default="40360")
    parser.addoption("--expected_station_name", action="store",default="Southport")