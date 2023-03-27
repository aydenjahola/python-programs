from tkinter import *

App = Tk()
App.title('Conversion App')
App.geometry('350x150')
scales = ['Celsius', 'Fahrenheit', 'Miles', 'Kilometres', 'Stones', 'Kilograms', 'Litres', 'Pints', 'Acres', 'Hectares']

_from = StringVar()
from_menu = OptionMenu(App, _from, *scales)
from_menu.grid(row=0, column=0, pady=5)

lbl = Label(App, text=' convert to ')
lbl.grid(row=0, column=1, pady=5)

to_ = StringVar()
to_menu = OptionMenu(App, to_, *scales)
to_menu.grid(row=0, column=2, pady=5)

enterL = Label(App, text='Enter your Value ')
enterL.grid(row=1, column=0, columnspan=2, pady=5)

numE = Entry(App)
numE.grid(row=1, column=2, columnspan=2, pady=5)

def converter():
    From = _from.get()
    To = to_.get()
    num = int(numE.get())

    if From == 'Celsius' and To == 'Fahrenheit':
        conv_num = 9.0 / 5.0 * num + 32
    elif From == 'Fahrenheit' and To == 'Celsius':
        conv_num = (num - 32.0) * 5.0 / 9.0
    elif From == 'Miles' and To == 'Kilometres':
        conv_num = num * 1.60934
    elif From == 'Kilometres' and To == 'Miles':
        conv_num = num * 0.621371
    elif From == 'Stones' and To == 'Kilograms':
        conv_num = num * 6.35029
    elif From == 'Kilograms' and To == 'Stones':
        conv_num = num * 0.157473
    elif From == 'Litres' and To == 'Pints':
        conv_num = num * 1.75975
    elif From == 'Pints' and To == 'Litres':
        conv_num = num * 0.568261
    elif From == 'Acres' and To == 'Hectares':
        conv_num = num * 0.404686
    elif From == 'Hectares' and To == 'Acres':
        conv_num = num * 2.47105
    else:
        conv_num = num

    numL = Label(App, text=round(conv_num,2), width=10)
    numL.grid(row=1, column=4, pady=5)


conB = Button(App, text='Convert', command=converter)
conB.grid(row=2, column=0, pady=5)

App.mainloop()
