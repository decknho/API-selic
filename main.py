import requests
import json

mes = {'01': 'janeiro', '02': 'fevereiro', '03': 'março',
       '04': 'abril', '05': 'maio', '06': 'junho',
       '07': 'julho', '08': 'agosto', '09': 'setembro',
       '10': 'outubro', '11': 'novembro', '12': 'dezembro'}
selic = requests.get("https://api.bcb.gov.br/dados/serie/bcdata.sgs.4189/dados?formato=json")
selic = selic.json()
mes_extenso = selic[-1]["data"]
mes_extenso = (mes_extenso[3] + mes_extenso[4])

print(f'{selic[-1]["data"]} | O valor do selic de {mes[mes_extenso]} está em {selic[-1]["valor"]}%')
