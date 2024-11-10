import pandas as pd
import requests
from matplotlib import pyplot as plt
from datetime import date

# Получаем текущую дату
today = date.today()

# Преобразуем её в строку в нужном формате
formatted_date = today.strftime('%Y-%m-%d')

j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/SBER/candles.json?from=2024-11-01&till='+formatted_date+'&interval=10').json()
data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]

print(data[0])
data[1]['year']=2024
data[1]['month']=2024
data[1]['day_in_week']=2024
data[1]['hour']=2024
data[1]['min']=2024
print(data[1])
#data[1].insert('year', 2024)
#print(data[1])

#pd.DataFrame(data).to_csv('files/sber_1h.csv')

"""
j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/YDEX/candles.json?from=2024-01-01&till='+formatted_date+'&interval=24').json()
data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]

pd.DataFrame(data).to_csv('files/ydex_1h.csv')


j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/TCSG/candles.json?from=2024-01-01&till='+formatted_date+'&interval=24').json()
data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]

pd.DataFrame(data).to_csv('files/tcsg_1h.csv')


j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/LKOH/candles.json?from=2024-01-01&till='+formatted_date+'&interval=24').json()
data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]

pd.DataFrame(data).to_csv('files/lkoh_1h.csv')


j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/AGRO/candles.json?from=2024-01-01&till='+formatted_date+'&interval=24').json()
data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]

pd.DataFrame(data).to_csv('files/agro_1h.csv')


j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/TATN/candles.json?from=2024-01-01&till='+formatted_date+'&interval=24').json()
data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]

pd.DataFrame(data).to_csv('files/tatn_1h.csv')


j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/TRNFP/candles.json?from=2024-01-01&till='+formatted_date+'&interval=24').json()
data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]

pd.DataFrame(data).to_csv('files/trnfp_1h.csv')


j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/CHMF/candles.json?from=2024-01-01&till='+formatted_date+'&interval=24').json()
data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]

pd.DataFrame(data).to_csv('files/chmf_1h.csv')


j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/MAGN/candles.json?from=2024-01-01&till='+formatted_date+'&interval=24').json()
data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]

pd.DataFrame(data).to_csv('files/magn_1h.csv')


j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/UPRO/candles.json?from=2024-01-01&till='+formatted_date+'&interval=24').json()
data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]

pd.DataFrame(data).to_csv('files/upro_1h.csv')

"""

#print(j)
#print(pd.DataFrame(data))


#frame = pd.DataFrame(data)
#plt.plot(list(frame['clos
# e']))
#plt.savefig("shares.png")