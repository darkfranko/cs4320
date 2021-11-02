from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pygal
from IPython.display import display
from datetime import datetime
import requests
import numpy as np
import pandas as pd
font1 = {'family':'serif','color':'blue','size':20}
apikey = "HZ259IH50LQMRCXN"
one = "TIME_SERIES_INTRADAY"
two = "TIME_SERIES_DAILY"
three = "TIME_SERIES_WEEKLY"
four = "TIME_SERIES_MONTHLY"
check = True
while check == True:
        # An input is requested and stored in a variable for what Symbol they want to use.
        print("Hello, Welcome to our Stock Data Visualizer.")
        symbolInput = str(input ("Enter the Stock Symbol you are looking for: "))
        # An input is requested and stored in a variable for what Chart they want to use.       
        print("\nChart Types\n-----------\n1. Line Graph\n2. Bar Graph\n")
        chartInput = int(input ("Enter the chart type you want(1,2): "))
        # An input is requested and stored in a variable for what Time Series they want to use.
        print("\nSelect the Time Series of the chart you want to Generate\n--------------------------------------------------------\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\n")
        tsInput = int(input ("Enter the Time Series option(1,2,3,4): "))
        # An input is requested and stored in a variable for what Start & End date they want to use.
<<<<<<< HEAD
        my_string_start_date = input('Enter start date(YYYY-MM-DD): ')
        my_date1 = datetime.strptime(my_string_start_date , "%Y-%m-%d")
        my_string_end_date = input('Enter end date(YYYY-MM-DD): ')
        my_date2 = datetime.strptime(my_string_end_date, "%Y-%m-%d")
        d0 = str(my_date1)
        d1 = str(my_date2)
        # ****** Idk where I went wrong with my code. => Francesko Saliaj ******
=======
        my_string_start_date = str(input('Enter start date(YYYY-MM-DD): '))
        my_date = datetime.strptime(my_string_start_date , "%Y-%m-%d")
        my_string_end_date = str(input('Enter end date(YYYY-MM-DD): '))
        my_date = datetime.strptime(my_string_end_date, "%Y-%m-%d")
        
        # Not sure where I went wrong. I would appreciate feedback please! => Francesko Saliaj
>>>>>>> ba740f92f8aa34d9c99791fd4f48ba767465ec82
        # Error Check:
        if (my_string_end_date<my_string_start_date):
            raise ValueError("You have an incorrect date range, please try again: ")
        if chartInput != 1 and chartInput != 2:
            raise ValueError("You have an incorrect input, please select number one or two: ")
        if tsInput != 1 and tsInput!= 2 and tsInput != 3 and tsInput != 4:
            raise ValueError("You have an incorrect input, please select number one, two, three, or four: ")
        if type(symbolInput) != str:
            raise ValueError("You have an incorrect input, please try again: ")

        # ***  if the user wants Bar graph: *** Can't figure out where I went wrong with pygal or matplotlib. Am highly requesting feedback as I was the only one to actually code for our team. => Francesko Saliaj
        if chartInput == 1:
            # chart = pygal.Bar()
            # chart.title = 'Stock Data for: ' + symbolInput + my_string_start_date + ' to ' + my_string_end_date
            # chart.x_labels = map(str, range(my_string_start_date, my_string_end_date))
            # chart.add('Open', [{'label': 'This is the Open bar.','color': 'red'}])
            # chart.add('High', [{'label': 'This is the High bar.','color': 'blue'}])
            # chart.add('Low', [{'label': 'This is the Low bar','color': 'green'}])
            # chart.add('Close', [{'label': 'This is the Close bar','color': 'yellow'}])
            # chart.render_in_browser()
            if tsInput == 1:
                url = 'https://www.alphavantage.co/query?function={one}&symbol={symbolInput}&interval=5min&apikey={apikey}'
                r = requests.get(url)
                data = r.json()
                #Draw the bar chart
                line_chart = pygal.Bar()
                line_chart.title = 'Intraday Times Series for the {symbolInput} stock (1 min) {my_string_start_date} to + {my_string_end_date}'
                # 
                line_chart = pygal.DateLine(x_label_rotation=45, range=(0, 750))
                line_chart.x_labels = [str(d0),str(d1)]
                line_chart.add('Open', data['open','color': 'red'].plot())
                line_chart.add('High', data['high', 'color': 'blue'].plot())
                line_chart.add('Low', data['low', 'color': 'green'].plot())
                line_chart.add('Close', data['close', 'color': 'yellow'].plot())
                line_chart.value_formatter = lambda x: '%.2f%%' % x if x is not None else '∅'
                line_chart.render()
                # ts = TimeSeries(key='HZ259IH50LQMRCXN', output_format='pandas')
                # x = ["Open", "High", "Low", "Close"]
                # y = [data['4. open','color': 'red'].plot(), data['4. high', 'color': 'blue'].plot(), data['4. low', 'color': 'green'].plot(), data['4. close', 'color': 'yellow'].plot()]
                # plt.barh(x, y)   
                # for index, value in enumerate(y):
                #     plt.text(value, index,
                #     str(value))    
                #     plt.show()
                check = False
            elif tsInput == 2:
                url = 'https://www.alphavantage.co/query?function={two}&symbol={symbolInput}&interval=5min&apikey={apikey}'
                r = requests.get(url)
                data = r.json()
                #Draw the bar chart
                line_chart = pygal.Bar()
                line_chart.title = 'Daily Times Series for the {symbolInput} stock (1 min) {my_string_start_date} to + {my_string_end_date}'
                line_chart.x_labels = map(str, range(int(my_string_start_date, my_string_end_date)))
                line_chart.add('Open', data['4. open','color': 'red'].plot())
                line_chart.add('High', data['4. high', 'color': 'blue'].plot())
                line_chart.add('Low', data['4. low', 'color': 'green'].plot())
                line_chart.add('Close', data['4. close', 'color': 'yellow'].plot())
                line_chart.value_formatter = lambda x: '%.2f%%' % x if x is not None else '∅'
                line_chart.render()
                # ts = TimeSeries(key='HZ259IH50LQMRCXN', output_format='pandas')
                # x = ["Open", "High", "Low", "Close"]
                # y = [data['4. open','color': 'red'].plot(), data['4. high', 'color': 'blue'].plot(), data['4. low', 'color': 'green'].plot(), data['4. close', 'color': 'yellow'].plot()]
                # plt.barh(x, y)
                # for index, value in enumerate(y):
                #     plt.text(value, index,
                #     str(value))
                #     plt.show()
                check = False
            elif tsInput == 3:
                url = 'https://www.alphavantage.co/query?function={three}&symbol={symbolInput}&interval=5min&apikey={apikey}'
                r = requests.get(url)
                data = r.json()
                #Draw the bar chart
                line_chart = pygal.Bar()
                line_chart.title = 'Weekly Times Series for the {symbolInput} stock (1 min) {my_string_start_date} to + {my_string_end_date}'
                line_chart.x_labels = map(str, range(int(my_string_start_date, my_string_end_date)))
                line_chart.add('Open', data['4. open','color': 'red'].plot())
                line_chart.add('High', data['4. high', 'color': 'blue'].plot())
                line_chart.add('Low', data['4. low', 'color': 'green'].plot())
                line_chart.add('Close', data['4. close', 'color': 'yellow'].plot())
                line_chart.value_formatter = lambda x: '%.2f%%' % x if x is not None else '∅'
                line_chart.render()
                # ts = TimeSeries(key='HZ259IH50LQMRCXN', output_format='pandas')
                # x = ["Open", "High", "Low", "Close"]
                # y = [data['4. open','color': 'red'].plot(), data['4. high', 'color': 'blue'].plot(), data['4. low', 'color': 'green'].plot(), data['4. close', 'color': 'yellow'].plot()]
                # plt.barh(x, y)
                # for index, value in enumerate(y):
                #     plt.text(value, index, str(value)) 
                #     plt.show()
                check = False
            elif tsInput == 4:
                url = 'https://www.alphavantage.co/query?function={four}&symbol={symbolInput}&interval=5min&apikey={apikey}'
                r = requests.get(url)
                data = r.json()
                #Draw the bar chart
                line_chart = pygal.Bar()
                line_chart.title = 'Monthly Times Series for the {symbolInput} stock (1 min) {my_string_start_date} to + {my_string_end_date}'
                line_chart.x_labels = map(str, range(int(my_string_start_date, my_string_end_date)))
                line_chart.add('Open', data['4. open','color': 'red'].plot())
                line_chart.add('High', data['4. high', 'color': 'blue'].plot())
                line_chart.add('Low', data['4. low', 'color': 'green'].plot())
                line_chart.add('Close', data['4. close', 'color': 'yellow'].plot())
                line_chart.value_formatter = lambda x: '%.2f%%' % x if x is not None else '∅'
                line_chart.render()
                # ts = TimeSeries(key='HZ259IH50LQMRCXN', output_format='pandas')
                # x = ["Open", "High", "Low", "Close"]
                # y = [data['4. open','color': 'red'].plot(), data['4. high', 'color': 'blue'].plot(), data['4. low', 'color': 'green'].plot(), data['4. close', 'color': 'yellow'].plot()]
                # plt.barh(x, y)
  
                # for index, value in enumerate(y):
                #     plt.text(value, index, str(value))
                #     plt.show()
                
                check = False
        elif chartInput == 2:
            if tsInput == 1:
                url = 'https://www.alphavantage.co/query?function={one}&symbol={symbolInput}&interval=5min&apikey={apikey}'
                r = requests.get(url)
                data = r.json()
                ts = TimeSeries(key='HZ259IH50LQMRCXN', output_format='pandas')
                data, meta_data = ts.get_intraday(symbol='{symbolInput}',interval='1min', outputsize='full')
                data['4. open','color': 'red'].plot()
                data['4. high', 'color': 'blue'].plot()
                data['4. low', 'color': 'green'].plot()
                data['4. close', 'color': 'yellow'].plot()
                plt.title('Intraday Times Series for the {symbolInput} stock (1 min) {my_string_start_date} to + {my_string_end_date}', fontdict = font1)
                plt.show()
                check = False
            elif tsInput == 2:
                url = 'https://www.alphavantage.co/query?function={two}&symbol={symbolInput}&interval=5min&apikey={apikey}'
                r = requests.get(url)
                data = r.json()
                ts = TimeSeries(key='HZ259IH50LQMRCXN', output_format='pandas')
                data, meta_data = ts.get_daily(symbol='{symbolInput}',interval='1min', outputsize='full')
                data['4. open','color': 'red'].plot()
                data['4. high', 'color': 'blue'].plot()
                data['4. low', 'color': 'green'].plot()
                data['4. close', 'color': 'yellow'].plot()
                plt.title('Intraday Times Series for the {symbolInput} stock (1 min) {my_string_start_date} to + {my_string_end_date}', fontdict = font1)
                plt.show()
                check = False
            elif tsInput == 3:
                url = 'https://www.alphavantage.co/query?function={three}&symbol={symbolInput}&interval=5min&apikey={apikey}'
                r = requests.get(url)
                data = r.json()
                ts = TimeSeries(key='HZ259IH50LQMRCXN', output_format='pandas')
                data, meta_data = ts.get_weekly(symbol='{symbolInput}',interval='1min', outputsize='full')
                data['4. open','color': 'red'].plot()
                data['4. high', 'color': 'blue'].plot()
                data['4. low', 'color': 'green'].plot()
                data['4. close', 'color': 'yellow'].plot()
                plt.title('Intraday Times Series for the {symbolInput} stock (1 min) {my_string_start_date} to + {my_string_end_date}', fontdict = font1)
                plt.show()
                check = False
            elif tsInput == 4:
                url = 'https://www.alphavantage.co/query?function={four}&symbol={symbolInput}&interval=5min&apikey={apikey}'
                r = requests.get(url)
                data = r.json()
                ts = TimeSeries(key='HZ259IH50LQMRCXN', output_format='pandas')
                data, meta_data = ts.get_monthly(symbol='{symbolInput}',interval='1min', outputsize='full')
                data['4. open','color': 'red'].plot()
                data['4. high', 'color': 'blue'].plot()
                data['4. low', 'color': 'green'].plot()
                data['4. close', 'color': 'yellow'].plot()
                plt.title('Intraday Times Series for the {symbolInput} stock (1 min) {my_string_start_date} to + {my_string_end_date}', fontdict = font1)
                plt.show()
                check = False
                
while check == False:
    x = print("Do you want to list a different Stock? (y/n): ")
    if x == "y" or x == "Y":
        check = True
    else:
        break
