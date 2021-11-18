import PySimpleGUI as sg
import pytest

TextSize = (60, 1)
layout = [
    [sg.Text("Welcome to my project", size=TextSize)], [sg.Text(
        "For this excerise I decided to test the Chicago Transit Authority API", size=TextSize)],
    [sg.Text("Like most useful APIs this requires an API key, this can be retrived easily from CTA's website", size=TextSize)],
    # add link if time
    # https://www.transitchicago.com/developers/
    [sg.Text("https://www.transitchicago.com/developers/")],
    [sg.Text("API Key", size=TextSize)],     # Part 2 - The Layout
    [sg.Input()],
    [sg.Button('Run Test')],


    # [sg.Output(size=(80, 20))]
]


# Create the window
window = sg.Window('CTA Tests Runner', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
# event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered


class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")
        print(dir(self.pytest_sessionfinish))

    def pytest_runtest_logreport(self, report):
        print(dir(report))


# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == "Run Test":
        retcode = pytest.main(
            ["-s",  "-x", "pytests", "--api_key", "aaa"], plugins=[MyPlugin()])
        print(vars(retcode))
        window.refresh()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

window.close()
