import os
import schedule
from time import sleep
from interface_grafica import DadosUsuario


def rodar_codigo(valor_monitorar):
    os.system(f'scrapy crawl dolar -a parametro={valor_monitorar}')

def wrapper():
    valor_monitorar = dados_usuario.get_valor_moeda()
    rodar_codigo(valor_monitorar)


dados_usuario = DadosUsuario()

if dados_usuario.button == 'Enviar':
    intervalo_envio = dados_usuario.get_intervalo_envio()
        
    if intervalo_envio == 'Minuto':
        schedule.every(1).minute.do(wrapper)
    elif intervalo_envio == 'Hora':
        schedule.every(1).hour.do(wrapper)
    elif intervalo_envio == 'Dia':
        schedule.every(1).day.do(wrapper)
    else:
        schedule.every(1).week.do(wrapper)

    os.chdir('variacao_dolar')
    print(str(schedule.next_run()))

    while True:
        schedule.run_pending()
        sleep(1)