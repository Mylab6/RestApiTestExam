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

    @pytest.fixture()
    def expected_station_name(self, pytestconfig):
        return pytestconfig.getoption("expected_station_name")

    def get_first_train(self, trainResp):
        return trainResp['ctatt']['eta'][0]
    
    def test_api_key_is_valid(self, api_key):
        # We can only validate for length
        assert len(api_key) == 32, 'Invalid API key. '

    def basic_arrival_request(self, api_key, mapid, numberOfTrains=1):
        query_params = {'key': api_key, 'max': numberOfTrains,
                        'mapid': mapid, 'outputType': 'JSON'}
        arrival_resp = requests.get(self.base_url, params=query_params)
        return arrival_resp

    def test_arrival_status_code(self, api_key,mapid):
        arrival_resp = self.basic_arrival_request(api_key, mapid)
        assert arrival_resp.status_code == 200

    def test_40360_station_name_is_Southport(self, api_key):
        arrival_resp = self.basic_arrival_request(api_key, 40360)
        trainResp = arrival_resp.json()
        first_train = self.get_first_train(trainResp)
        assert first_train['staNm'] == "Southport"

    def test_dynamtic_mapid(self, api_key, mapid,expected_station_name):
        arrival_resp = self.basic_arrival_request(api_key, mapid)
        trainResp = arrival_resp.json()      
        try:
            first_train = self.get_first_train(trainResp)
            assert first_train['staNm'] == expected_station_name
        except:
            assert False, str(mapid) + ' is not a valid mapid or has no comming arrivals '