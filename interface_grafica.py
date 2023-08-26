import PySimpleGUI as sg




class DadosUsuario:

    def __init__(self):
        
        sg.theme('DarkGreen1')

        layout = [
            
            [sg.Text('Quero receber atualizações de preço a cada: ', 
            font=('Helvetica', 14), text_color=('#FFFFFF'))],

            [sg.Radio("Minuto", group_id="intervalo_envio", default=True), sg.Radio("Hora", group_id="intervalo_envio"), sg.Radio("Dia", group_id="intervalo_envio"), sg.Radio("Semana", group_id="intervalo_envio")],

            [sg.Text('Desejo receber e-mails quando o dólar estiver acima de: ', 
            font=('Helvetica', 14), text_color=('#FFFFFF'))],

            [sg.Radio("R$ 3,50", group_id="valor_moeda", default=True), sg.Radio("R$ 4,00", group_id="valor_moeda"), sg.Radio("R$ 4,25", group_id="valor_moeda"), sg.Radio("R$ 4,50", group_id="valor_moeda"), sg.Radio("R$ 4,75", group_id="valor_moeda"), sg.Radio("R$ 5,00", group_id="valor_moeda") ],
            
            [sg.Button('Enviar', button_color=('white', '#45D669'), 
            font=('Helvetica', 14)), 
             sg.Button('Cancelar', button_color=('white', 'red'), 
            font=('Helvetica', 14))]
        
        ]

        janela = sg.Window('Dados do Usuário:', font='_ 14', size=(670,200))\
        .layout(layout)

        
	
        self.button, self.values = janela.Read() 
        janela.close()

    def get_intervalo_envio(self):
        tempo_envio = {
            0: 'Minuto',
            1: 'Hora',
            2: 'Dia',
            3: 'Semana'
        }
        for chave in self.values:
            if chave in (0, 1, 2, 3, 4) and self.values[chave]:
                return tempo_envio[chave]
 
    def get_valor_moeda(self):
        valor_monitoravel = {
            4: 3.50,
            5: 4.00,
            6: 4.25,
            7: 4.50,
            8: 4.75,
            9: 5.00
        }
        for chave in self.values:
            if chave in (5, 6, 7, 8, 9, 10) and self.values[chave]:
                    return valor_monitoravel[chave]

    


