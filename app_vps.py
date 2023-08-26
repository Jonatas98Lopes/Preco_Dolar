import os
import schedule
from time import sleep


def rodar_codigo():
    os.system(f'scrapy crawl dolar -a parametro={valor_monitorar}')



"""
intervalo_envio = você define o intervalo de tempo de envio -email: 
-Minuto: a cada um minuto; Hora: a cada uma hora. 
Dia: uma vez a cada dia; Semana: uma vez a cada semana."""
intervalo_envio = 'Minuto'

"""valor_monitorar: O e-mail só será enviado se o valor do dólar 
estiver acima deste parâmetro. Digite um valor decimal."""
valor_monitorar = 4.75


if intervalo_envio == 'Minuto':
    schedule.every(1).minute.do(rodar_codigo)
elif intervalo_envio == 'Hora':
    schedule.every(1).hour.do(rodar_codigo)
elif intervalo_envio == 'Dia':
    schedule.every(1).day.do(rodar_codigo)
else:
    schedule.every(1).week.do(rodar_codigo)

os.chdir('variacao_dolar')
print(str(schedule.next_run()))

while True:
    schedule.run_pending()
    sleep(1)