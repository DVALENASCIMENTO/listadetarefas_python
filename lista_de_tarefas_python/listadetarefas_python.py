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


# criar a janela
janela = criar_janela_inicial()

# criar as regras dessa janela
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()