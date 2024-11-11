import pandas as pd
import requests
import datetime
from matplotlib import pyplot as plt
from datetime import date


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Item(name='{self.name}', value={self.value})"

def main(instr):

    today = date.today()

    # Преобразуем её в строку в нужном формате
    formatted_date = today.strftime('%Y-%m-%d')

    j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/'+instr+'/candles.json?from=2024-10-01&till='+formatted_date+'&interval=10').json()
    data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]

    #for index, value in enumerate(my_list):
    #    print(f'Элемент {index}: {value}')

        
    # Перебираем массив и добавляем новый объект в каждый элемент
    new_items = []
    for item in data:
        dt_begin = datetime.datetime.strptime(item['begin'], "%Y-%m-%d %H:%M:%S")
        dt_end = datetime.datetime.strptime(item['end'], "%Y-%m-%d %H:%M:%S")
        # Извлекаем нужные значения
        year = dt_begin.year
        month = dt_begin.month
        week = dt_begin.isocalendar()[1]
        hour = dt_begin.hour
        minute_begin = dt_begin.minute
        minute_end = dt_end.minute
        day_in_week = dt_begin.isoweekday()
        item['year']=year;
        item['month']=month;
        item['week']=week;
        item['day_in_week']=day_in_week;
        item['hour']=hour;
        item['min_begin']=minute_begin;
        item['min_end']=minute_end;
        new_items.append(item)
        #new_item = Item(f"new_{item.name}", item.value + 500)
        #new_items.append(new_item)
        
        
    # Объединяем исходный массив с новым
    #result = data + new_items
    
    # Выводим результат
    pd.DataFrame(data).to_csv('files/'+instr+'_10min.csv')
    print('Save - '+instr+'_10min.csv')

if __name__ == "__main__":    
    main('YDEX')
    main('SBER')
    main('TCSG')
    main('LKOH')
    main('AGRO')
    main('TATN')
    main('TRNFP')
    main('CHMF')
    main('MAGN')
    main('UPRO')

# Получаем текущую дату

#print(data[1])
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