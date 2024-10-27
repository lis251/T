import pandas as pd
import requests
from matplotlib import pyplot as plt
from datetime import date

# Получаем текущую дату
today = date.today()

# Преобразуем её в строку в нужном формате
formatted_date = today.strftime('%Y-%m-%d')

j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/SBER/candles.json?from=2024-01-01&till='+formatted_date+'&interval=24').json()
data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]

pd.DataFrame(data).to_csv('files/sber.csv')


j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/YDEX/candles.json?from=2024-01-01&till='+formatted_date+'&interval=24').json()
data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]

pd.DataFrame(data).to_csv('files/ydex.csv')


j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/TCSG/candles.json?from=2024-01-01&till='+formatted_date+'&interval=24').json()
data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]

pd.DataFrame(data).to_csv('files/tcsg.csv')

#print(j)
#print(pd.DataFrame(data))


#frame = pd.DataFrame(data)
#plt.plot(list(frame['clos
# e']))
#plt.savefig("shares.png")