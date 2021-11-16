import PySimpleGUI as sg                       

import pytest
layout = [ 
     [sg.Text("Welcome to my project , for this excerise I decided to test the Chicago Transit Authority API \n Like most useful APIs this requires an API key, this can be retrived easily from CTA's website")] ,    
   # add link if time 
   # https://www.transitchicago.com/developers/
    [sg.Text("https://www.transitchicago.com/developers/")],
     [sg.Text("API Key")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Button('Run Test')] , 
            
            
           # [sg.Output(size=(80, 20))]
            ]
            

# Create the window
window = sg.Window('CTA Tests Runner', layout)      # Part 3 - Window Defintion
                                                
# Display and interact with the Window
#event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered


# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == "Run Test":
      retcode = pytest.main(["-s",  "-x","pytests","--api_key","aaa"])
      print(retcode)
      window.refresh()
    
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    #window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")


#print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()   