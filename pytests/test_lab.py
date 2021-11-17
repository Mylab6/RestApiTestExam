import pytest
import requests

class TestCtaAPI:
    base_url = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx"
    @pytest.fixture()
    def api_key(self, pytestconfig):
        return pytestconfig.getoption("api_key")

    def test_api_key_is_valid(self,api_key):
        # We can only validate for length     
        assert len(api_key) == 32, 'Invalid API key. '
    def basic_arrival_request(self,api_key,mapid):
        query_params = {'key':api_key,'max':1,'mapid':mapid, 'outputType':'JSON'}
        arrival_resp = requests.get(self.base_url,params=query_params)
        return arrival_resp

    def test_arrival_status_code(self, api_key):
        arrival_resp = self.basic_arrival_request(api_key,40360)
        assert arrival_resp.status_code == 200 
    def test_arrival_to_Kimble(self,api_key):
        arrival_resp = self.basic_arrival_request(api_key,40360)
        text = arrival_resp.json()
        print(text)
