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

saldo = float(input("Quantos reais por mês você pretende investir? "))
saldo_mensal = saldo
anos = int(input("Quantidade de anos que você pretende investir? "))
meses = anos * 12
porcentagem_selic_mes = float(selic[-1]['valor']) / 12
contador_de_mes = 2
guardou = saldo * meses
print(f"Saldo inicial R${saldo}")
print(f"Quantidade de anos: {anos}")
while meses != 1:
    saldo = saldo + saldo_mensal + (saldo / 100 * porcentagem_selic_mes)
    print(f"{contador_de_mes}° MÊS R${saldo: .2f}".replace('.', ','))
    contador_de_mes += 1
    meses -= 1
print(f"você guardou R${guardou}")
rendeu = saldo - guardou
print(f"{rendeu: .2f}")
