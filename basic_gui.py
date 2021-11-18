import PySimpleGUI as sg
import pytest
import json
import webbrowser
from datetime import datetime


TextSize = (100, 1)
sg.theme('Black')
init_map_id = 40360
init_station_name = 'Southport'
sample_train_stops = {"Lake": 41660, 'Western': 41480, 'Southport': 40360}
train_buttons = list(map(lambda train_stop_name: sg.Button(
    train_stop_name), sample_train_stops.keys()))

cta_dev_url = "https://www.transitchicago.com/developers/"
layout = [
    [sg.Text("Welcome to my project", size=TextSize)], [sg.Text(
        "For this excerise I decided to test the Chicago Transit Authority API", size=TextSize)],
    [sg.Text("Like most APIs, this requires an API key, this can be retrived easily from CTA's website", size=TextSize)],
    [sg.Text("Make sure you get a train arrivals api key", size=TextSize)],

    # add link if time
    # https://www.transitchicago.com/developers/
    [sg.Button(cta_dev_url)],
    [sg.Text("Mapid"), sg.Input(init_map_id, key="mapid")],
    [sg.Text("Expected Station Name"), sg.Input(
        init_station_name, key="expected_station_name")],
    [sg.Text("Select Station",size=TextSize)],
    train_buttons,
    [sg.Text("API Key"), sg.Input(key="api_key")],
    [sg.Button('Run Test')],
    [sg.Multiline('Waiting for test data \n', size=(70,30), key="Testoutput" )]


    # [sg.Output(size=(80, 20))]
]


# Create the window
window = sg.Window('CTA Tests Runner', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
# event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered

def print_to_multi_line(string_to_write):
     window["Testoutput"].print(string_to_write)
     window.refresh()
class GetTestResults:

    def pytest_sessionfinish(self):
        #return
        window["Testoutput"].println(dir(self.pytest_sessionfinish) )
        window.refresh()


# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed

    if event in sample_train_stops:
        window.Element("mapid").update(sample_train_stops[event])
        window.Element("expected_station_name").update(event)
        #init_map_id = sample_train_stops[event]
        window.refresh()
    if event == "Run Test":
        retcode = pytest.main(
            [ "-s",  "pytests", "--json-report",  "--api_key", values['api_key'], "--mapid", values['mapid'], "--expected_station_name",values['expected_station_name']  ])       

      
 

        json_file = open('.report.json')
        json_result = json.load(json_file)

        dt_object = datetime.fromtimestamp(json_result["created"])
        print_to_multi_line("Ran at :" + str( dt_object) )
        for key, val  in json_result["summary"].items():           
            print_to_multi_line(key +" : " +  str(val))
        for test_result in json_result["tests"]:
            print_to_multi_line("Test: "+ test_result["nodeid"] )
            print_to_multi_line("Result: "+ test_result["outcome"] )      
            if "traceback" in  test_result["call"]:
                print_to_multi_line("Message: "+ test_result["call"]["traceback"][0]["message"] )


 


        
        window.refresh()
    if event == cta_dev_url:
         webbrowser.open(cta_dev_url)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

window.close()
