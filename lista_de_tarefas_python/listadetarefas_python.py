import PySimpleGUI as sg


# Criando o layout
def criar_janela_inicial():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas', Layout=linha, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]

    return sg.Window('Todo List', Layout=layout, finalize=True)

# Layout nova tarefa
def nova_tarefa():
    #Layout que será mostrado:
    layout = [[sg.Text('Titulo')],
              [sg.Input()],
              [sg.Button('Sair', key='sair'), sg.Button('Salvar', key='nTarefa')]]
    window = sg.Window('Nova tarefa', layout, icon=r'icon.ico')
    event, values = window.read()
    while True:
        if event == 'nTarefa':
            # Vai printar o valor digitado no input
            print(values[0])
            break
        elif event in (sg.WINDOW_CLOSED, 'sair'):
            window.close()
            break
            
# criar a janela
janela = criar_janela_inicial()

# criar as regras dessa janela
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        nova_tarefa()
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()
