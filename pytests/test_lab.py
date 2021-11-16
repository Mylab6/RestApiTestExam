import pytest

@pytest.fixture()
def api_key(pytestconfig):
    return pytestconfig.getoption("api_key")

def test_print_name(api_key):
        print(f"\ncommand line param (name): {api_key}")

def test_print_name_2(pytestconfig):
    print(f"test_print_name_2(api_key): {pytestconfig.getoption('api_key')}")