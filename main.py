import PySimpleGUI as sg
from tela_home import tela_menu
from tela_escolha import tela_inicial
from tela_sim import sim

nome = ""
forca = 0
click = 0
nada = 0

menu = tela_menu()


while True:
    janela, evento, valores = sg.read_all_windows()

    
    if evento == "Iniciar":
        nome = valores['nome']
        menu.hide()
        menu = tela_inicial()
    
    if evento == 'Escolher':
        if valores[0]:
            menu.hide()
            menu = sim(click)
        else:
            print("Seu cagão")
    
    if evento == 'Treinar':
        print("treinou!")
        forca += 1
        click += 1
    if evento == "Meditar":
        print("meditou!")
        forca += 2
        click += 1
    if evento == "Nada":
        nada += 1
        click += 1
    
    if click == 5:
        menu.hide()
        menu = sim(click)



            
    
    

    if janela == menu and evento == sg.WINDOW_CLOSED:
        break
    
