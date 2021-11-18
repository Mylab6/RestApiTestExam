import PySimpleGUI as sg
import pytest

TextSize = (100, 1)
sg.theme('DarkGrey')

layout = [
    [sg.Text("Welcome to my project", size=TextSize)], [sg.Text(
        "For this excerise I decided to test the Chicago Transit Authority API", size=TextSize)],
    [sg.Text("Like most APIs this requires an API key, this can be retrived easily from CTA's website", size=TextSize)],
    # add link if time
    # https://www.transitchicago.com/developers/
    [sg.Text("https://www.transitchicago.com/developers/",size=TextSize )],
    [sg.Text("API Key", size=TextSize)],     # Part 2 - The Layout
    [sg.Input(key="api_key")],
    [sg.Input('40360',key="mapid")],

    [sg.Button('Run Test', size=TextSize )],


    # [sg.Output(size=(80, 20))]
]


# Create the window
window = sg.Window('CTA Tests Runner', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
# event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered


class MyPlugin:
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
    if event == "Run Test":
        retcode = pytest.main(
            ["-s",  "-x", "pytests", "--api_key", values['api_key'],"--mapid",values['mapid'] ], plugins=[MyPlugin()])
        print(vars(retcode))
        window.refresh()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

window.close()
