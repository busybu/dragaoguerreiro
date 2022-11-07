import PySimpleGUI as sg

def tela_inicial():
    sg.theme('DarkRed')
    layout =[
        [sg.Text("Você deseja ser o dragão guerreiro?", font='Tangerine')],
        [sg.Radio('Sim', 'sim'),sg.Radio('Não','sim')],
        [sg.Button('Escolher')]
    ]
    return sg.Window('Home Screen', layout=layout, finalize=True, element_justification= 'c')

