import pytest
import requests


class TestCtaAPI:
    base_url = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx"

    @pytest.fixture()
    def api_key(self, pytestconfig):
        return pytestconfig.getoption("api_key")

    @pytest.fixture()
    def mapid(self, pytestconfig):
        return pytestconfig.getoption("mapid")

    def test_api_key_is_valid(self, api_key):
        # We can only validate for length
        assert len(api_key) == 32, 'Invalid API key. '

    def basic_arrival_request(self, api_key, mapid, numberOfTrains=1):
        query_params = {'key': api_key, 'max': numberOfTrains,
                        'mapid': mapid, 'outputType': 'JSON'}
        arrival_resp = requests.get(self.base_url, params=query_params)
        return arrival_resp

    def test_arrival_status_code(self, api_key):
        arrival_resp = self.basic_arrival_request(api_key, 40360)
        assert arrival_resp.status_code == 200

    def test_station_name_is_Southport(self, api_key):
        arrival_resp = self.basic_arrival_request(api_key, 40360, 3)
        trainResp = arrival_resp.json()
        for trainArrival in trainResp['ctatt']['eta']:
            assert trainArrival['staNm'] == "Southport"

    def test_dynamtic_mapid(self, api_key, mapid):
        arrival_resp = self.basic_arrival_request(api_key, mapid, 3)
        trainResp = arrival_resp.json()
        assert arrival_resp.status_code == 200
        try:
            for trainArrival in trainResp['ctatt']['eta']:
                assert trainArrival['staNm'] is not None
        except:
            assert False, str(mapid) + ' is not a valid mapid or has no comming arrivals '