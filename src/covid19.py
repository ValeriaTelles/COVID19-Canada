import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator
from matplotlib.widgets import Cursor
from matplotlib.dates import DateFormatter

""" Loading and Selecting Data """
df = pd.read_csv('https://health-infobase.canada.ca/src/data/covidLive/covid19.csv')
df['date'] = pd.to_datetime(df['date'], format = '%d-%m-%Y')
locations = ['Ontario', 'British Columbia', 'Quebec', 'Alberta', 'Saskatchewan', 'Manitoba', 'New Brunswick', 'Nova Scotia', 'Prince Edward Island', 'Newfoundland and Labrador', 'Yukon', 'Northwest Territories', 'Nunavut']
df = df[df['prname'].isin(locations)] # creating a bool series from isin()

""" Reconstructing the Data """
df = df.pivot(index='date', columns='prname', values='numtoday')
locations = list(df.columns)
covid = df.reset_index('date')
covid.set_index(['date'], inplace=True)
covid.columns = locations

""" Generating Colors and Style """
colors = ['#E6194B', '#F58231', '#FFE119', '#BFEF45', '#F032E6', '#000075', '#469990', '#911EB4', '#3CB44B', '#42D4F4', '#4363D8', '#D9B5FF', '#B83394']
plt.style.use('classic')

""" Creating the Visualization """
txtstr = 'Source: https://health-infobase.canada.ca/src/data/covidLive/covid19.csv'

plot = covid.plot(figsize=(15,9), color=colors, linewidth=2, legend=True)
plot.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plot.grid(color='#D8D8D8')
plot.legend(bbox_to_anchor=(1.04,0.5), loc='center left')
plot.set_xlabel('Date', fontweight='bold', fontsize=15, labelpad=15)
plot.set_ylabel('Number of Cases', fontweight='bold', fontsize=15, labelpad=15)
plot.set_title('COVID-19 Daily Cases by Province and Territory in Canada', fontweight='bold', fontsize=24, pad=24)
plot.set_ylim(bottom=-25)
plot.text(covid.index[0], -400, txtstr.rjust(104), fontweight='bold', fontsize=11)
plt.xticks(rotation=0)

months =  mdates.MonthLocator() 
days = mdates.DayLocator()
fmt = mdates.DateFormatter('%b') 

plot.xaxis.set_major_locator(months)
plot.xaxis.set_minor_locator(days)
plot.xaxis.set_major_formatter(fmt)
plot.yaxis.set_minor_locator(MultipleLocator(50))

cursor = Cursor(plot, useblit=False, color='#666666', linewidth=0.8, linestyle='dashed')

plt.tight_layout()
plt.show()