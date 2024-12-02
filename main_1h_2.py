import pandas as pd
import requests
import datetime
from matplotlib import pyplot as plt
from datetime import datetime, timedelta
import sys
import csv


i_day_close=1
cost_day_close=0
cost_day_close_tmp=0
i_day_open=1
cost_day_open=0
i_week_close=1
cost_week_close=0
i_week_open=1
cost_week_opene=0


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Item(name='{self.name}', value={self.value})"

def main(instr,dateStart,dateEnd):

    #today = date.today()

    # Преобразуем её в строку в нужном формате
    #formatted_date = today.strftime('%Y-%m-%d')

    j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/'+instr+'/candles.json?from='+dateStart+'&interval=10').json()
    data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]

    #for index, value in enumerate(my_list):
    #    print(f'Элемент {index}: {value}')

        
    # Перебираем массив и добавляем новый объект в каждый элемент
    new_items = []
    for item in data:        
        dt_begin = datetime.strptime(item['begin'], "%Y-%m-%d %H:%M:%S")
        dt_end = datetime.strptime(item['end'], "%Y-%m-%d %H:%M:%S")
        # Извлекаем нужные значения
        year = dt_begin.year
        month = dt_begin.month
        week = dt_begin.isocalendar()[1]
        hour = dt_begin.hour
        minute_begin = dt_begin.minute
        minute_end = dt_end.minute
        day_in_week = dt_begin.isoweekday()
        day_of_year = dt_begin.timetuple().tm_yday
        item['year']=year;
        item['month']=month;
        item['week']=week;
        item['day_in_week']=day_in_week;
        item['day_in_year']=day_of_year;
        item['hour']=hour;
        item['min_begin']=minute_begin;
        item['min_end']=minute_end;
        if dateEnd<dt_begin:
            new_items.append(item)

        # calc close prev day
        i_day_close=day_in_week

        #new_item = Item(f"new_{item.name}", item.value + 500)
        #new_items.append(new_item)

        if i_day_close==1:
            i_day_close=day_of_year
            item['back_close_day']=0

        if i_day_close<day_in_year:
            cost_day_close=cost_day_close_tmp
            i_day_close=day_in_year
            item['back_close_day']=cost_day_close
        else
            item['back_close_day']=cost_day_close
            

        cost_day_close_tmp=item['close']

        

    return new_items;
        
        
    # Объединяем исходный массив с новым
    #result = data + new_items
    
    # Выводим результат
    #pd.DataFrame(data).to_csv('files/'+instr+'_10min.csv')
    #print('Save - '+instr+'_10min.csv')

if __name__ == "__main__":   

    arguments = sys.argv[1:]
    days = arguments[0]

    instrAll= ['YDEX','SBER','TCSG','LKOH','AGRO','TATN','TRNFP','CHMF','MAGN','UPRO','OZON','MTS']

    pd.DataFrame(instrAll).to_csv('files/instr_all.csv', index = False,header = False)

    for instr in instrAll:


        # Устанавливаем начальную дату
        #start_date = datetime(2024, 1, 1)
        
        stepSart = timedelta(days=int(days))
        start_date = datetime.now()-stepSart
        current_date = datetime.now()
        step = timedelta(days=4)

        date = start_date
        dataAll = []
        while date <= current_date:
            formatted_date = date.strftime("%Y-%m-%d")
            #print(formatted_date)
            dataAll=dataAll+main(instr,formatted_date,date+step);    
            date += step
        
        pd.DataFrame(dataAll).to_csv('files/'+instr+'_10min.csv')
        print('Save - '+instr+'_10min.csv')
    


    """
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
    """

