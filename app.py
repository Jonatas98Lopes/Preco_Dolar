import os
import schedule
from time import sleep

def rodar_codigo():
    os.system('scrapy crawl dolar')

print(os.getcwd())
os.chdir('variacao_dolar')
schedule.every(1).mo
schedule.every(1).minute.do(rodar_codigo)
print(str(schedule.next_run ()))

while True:
    schedule.run_pending()
    sleep(1)