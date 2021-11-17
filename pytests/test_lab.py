import pytest
import requests

class TestCtaAPI:
    base_url = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx"
    @pytest.fixture()
    def api_key(self, pytestconfig):
        return pytestconfig.getoption("api_key")

    def test_print_name(self,api_key):
        query_params = {'key':api_key,'max':1,'mapid':40360, 'outputType':'JSON'}
        r = requests.get(self.base_url,params=query_params)
        text = r.json()
        print(text)
        assert r.status_code == 200 

    def test_print_name_2(self,pytestconfig):
        print(f"test_print_name_2(api_key): {pytestconfig.getoption('api_key')}")