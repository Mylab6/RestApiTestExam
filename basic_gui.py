import PySimpleGUI as sg
import pytest

TextSize = (100, 1)
sg.theme('Black')
init_map_id = 40360
init_station_name = 'Southport'
sample_train_stops = {"Lake": 41660, 'Western': 41480, 'Southport': 40360}
train_buttons = list(map(lambda train_stop_name: sg.Button(
    train_stop_name), sample_train_stops.keys()))

layout = [
    [sg.Text("Welcome to my project", size=TextSize)], [sg.Text(
        "For this excerise I decided to test the Chicago Transit Authority API", size=TextSize)],
    [sg.Text("Like most APIs this requires an API key, this can be retrived easily from CTA's website", size=TextSize)],
    # add link if time
    # https://www.transitchicago.com/developers/
    [sg.Text("https://www.transitchicago.com/developers/", size=TextSize)],
    [sg.Text("Mapid"), sg.Input(init_map_id, key="mapid")],
    [sg.Text("Expected Station Name"), sg.Input(
        init_station_name, key="expected_station_name")],
    [sg.Text("Select Station",size=TextSize)],
    train_buttons,
    [sg.Text("API Key"), sg.Input(key="api_key")],
    [sg.Button('Run Test')],


    # [sg.Output(size=(80, 20))]
]


# Create the window
window = sg.Window('CTA Tests Runner', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
# event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered


class GetTestResults:
    def pytest_sessionfinish(self):
        return
        print("*** test run reporting finishing")
        print(dir(self.pytest_sessionfinish))

    def pytest_runtest_logreport(self, report):
        print(report.outcome)


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
            ["-s",  "pytests", "--api_key", values['api_key'], "--mapid", values['mapid'], "--expected_station_name",values['expected_station_name']  ], plugins=[GetTestResults()])
        print(vars(retcode))
        window.refresh()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

window.close()
