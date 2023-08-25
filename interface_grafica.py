import PySimpleGUI as sg




class DadosUsuario:

    def __init__(self):
        
        sg.theme('DarkGreen1')

        layout = [
            
            [sg.Text('Quero receber atualizações de preço a cada: ', 
            font=('Helvetica', 14), text_color=('#FFFFFF'))],

            [sg.Radio("Minuto", "intervalo_envio", default=True), sg.Radio("Hora", "intervalo_envio"), sg.Radio("Dia", "intervalo_envio"), sg.Radio("Semana", "intervalo_envio"), sg.Radio("Mês", "intervalo_envio")],

            [sg.Text('Desejo receber e-mails quando o dólar estiver acima de: ', 
            font=('Helvetica', 14), text_color=('#FFFFFF'))],

            [sg.Radio("R$ 3,50", "valor_moeda", default=True), sg.Radio("R$ 4,00", "valor_moeda"), sg.Radio("R$ 4,25", "valor_moeda"), sg.Radio("R$ 4,50", "valor_moeda"), sg.Radio("R$ 4,75", "valor_moeda"), sg.Radio("R$ 5,00", "valor_moeda") ],
            
    
            [sg.Button('Enviar', button_color=('white', '#45D669'), 
            font=('Helvetica', 14)), 
             sg.Button('Cancelar', button_color=('white', 'red'), 
            font=('Helvetica', 14))]
        ]

        janela = sg.Window('Dados do Usuário:', font='_ 14', size=(670,200))\
        .layout(layout)

	
        self.button, self.values = janela.Read() 
        janela.close()

