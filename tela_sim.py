import PySimpleGUI as sg

def sim(clicked):
    sg.theme('DarkRed')
    layout =[
        [sg.Text("ᓚᘏᗢ Escolha uma opção (❁´◡`❁)", font='Tangerine')],
        [sg.Button('Treinar')],
        [sg.Button('Meditar')],
        [sg.Button('Nada')]
    ] if clicked == 0 else [
        
        [sg.Text("ᓚᘏᗢ Escolha uma opção (❁´◡`❁)", font='Tangerine')],
        [sg.Button('Treinar')],
        [sg.Button('Meditar')],
        [sg.Button('Nada')]
        [sg.Button('Avançar')]
    ]
    return sg.Window('Dragão Guerreiro', layout=layout, finalize=True, element_justification= 'c')

