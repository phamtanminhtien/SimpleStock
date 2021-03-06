from pandas_datareader import data
import datetime
from  bokeh.plotting import figure, show, output_file

start_date = datetime.datetime(2019, 6, 1)
end_date = datetime.datetime(2019, 12, 15)
df = data.DataReader(name = "GOOG", data_source = "yahoo", start = start_date, end = end_date)

def inc_dec(c , o):
    if c > o:
        value = "Increase"
    elif c < o :
        value = "Decrease"
    else :
        value = "Equal"
    return value

df["Status"] = [inc_dec(c , o) for c, o in zip(df.Close, df.Open)]
df["Middle"] = (df.Open+df.Close) / 2
df["Height"] = abs(df.Close - df.Open)

p = figure(x_axis_type='datetime', width = 1000, height = 300)
p.title.text = "Candlestick Chart"

hours_12 = 12*60*60*1000

#tăng
p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],
   hours_12, df.Height[df.Status=="Increase"],fill_color="#CCFFFF",
   line_color="black")
#giảm
p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],
   hours_12, df.Height[df.Status=="Decrease"],fill_color="#FF3333",
   line_color="black")
p.segment(df.index, df.High, df.index, df.Low, color="Black")
output_file("chart.html")
show(p)