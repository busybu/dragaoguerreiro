import PySimpleGUI as sg

def tela_menu():
    sg.theme('DarkRed')
    layout =[
        [sg.Text("(❁´◡`❁) Kung Fu Panda Amor Doce ☆*", font='Tangerine')],
        [sg.Input("Entre com o nome do dragão guerreiro", key="nome", do_not_clear=False)],
        [sg.Button('Iniciar')]
    ]
    return sg.Window('Home Screen', layout=layout, finalize=True, element_justification= 'c')

