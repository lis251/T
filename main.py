import pandas as pd
import requests
from matplotlib import pyplot as plt

j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/SBER/candles.json?from=2024-01-01&till=2024-10-26&interval=24').json()
data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]

pd.DataFrame(data).to_csv('files/sber.csv')
#print(j)
print(pd.DataFrame(data))


#frame = pd.DataFrame(data)
#plt.plot(list(frame['clos
# e']))
#plt.savefig("shares.png")