#---------------------logic behind the code------------------------------
# The main function used to convert the temperature is tempconv(). The formula used to convert temperature if
# K = C + 273.15, F = (9/5)*C + 32. The temperature is rounded upto 3 digits.


#---------------------------------program--------------------------------

from tkinter import *

def tempconv(temp, unit):
    if unit == 'Celsius':
        Ctemp = temp
        Ktemp = temp + 273.15
        Ftemp = (9 / 5) * temp + 32
    elif unit == 'Fahrenheit':
        Ctemp = (temp - 32) * (5 / 9)
        Ktemp = Ctemp + 273.15
        Ftemp = temp
    elif unit == 'Kelvin':
        Ctemp = temp - 273.15
        Ktemp = temp
        Ftemp = (9 / 5) * Ctemp + 32
    return round(Ctemp,3), round(Ktemp, 3), round(Ftemp, 3)

class App(Tk):
    def __init__(self):
        super().__init__()
        self.heading = Label(self, text='Temperature Converter', bg='light salmon', font='algerian 30',justify='center',
                            border=20, relief=GROOVE, padx=20, pady=10)
        self.temp = StringVar()  # variable to store the user input -> temperature
        self.temp.trace("w", self.show_message)
        self.tempinp = Entry(self, textvariable=self.temp, font='bold 20', justify='center', relief=RIDGE,
                             border=20, bg='LavenderBlush')
        self.unit = StringVar()  # variable to store the unit used in the checkbox
        self.unit.set("Celsius")
        self.tempunit = OptionMenu(self, self.unit, "Celsius", "Fahrenheit", "Kelvin")
        self.heading.pack(fill=X)
        self.tempinp.place(x=170, y=110)
        self.tempunit.place(x=550, y=110)
        self.tempunit.config(height=1, font='felixtitling 30', bg='LightCyan', relief=SUNKEN, border=10,
                        activebackground='pink')
        self.ctemplabel = Label(self, relief=GROOVE, text='', font='cooperblack 20', border=15, width=15)
        self.ktemplabel = Label(self, relief=GROOVE, text='', font='cooperblack 20', border=15, width=15)
        self.ftemplabel = Label(self, relief=GROOVE, text='', font='cooperblack 20', border=15, width=15)
        self.ctemplabel.place(x=0, y=300)
        self.ktemplabel.place(x=300, y=300)
        self.ftemplabel.place(x=600, y=300)
        self.celsiuslabel = Label(self, relief=GROOVE, text='Celsius', font='cooperblack 20', border=15, width=15)
        self.kelvinlabel = Label(self, relief=GROOVE, text='Kelvin', font='cooperblack 20', border=15, width=15)
        self.fahrenheitlabel = Label(self, relief=GROOVE, text='Fahrenheit', font='cooperblack 20', border=15, width=15)
        self.celsiuslabel.place(x=0, y=400)
        self.kelvinlabel.place(x=300, y=400)
        self.fahrenheitlabel.place(x=600,y=400)

    def show_message(self, *args):
        TEMP = self.temp.get()  # getting the temperature from the user
        UNIT = self.unit.get()  # getting the unit from the checkbox
        try:
            TEMP = float(TEMP)
            CTEMP, KTEMP, FTEMP = tempconv(TEMP, UNIT)
            self.ctemplabel.config(text=str(CTEMP))
            self.ktemplabel.config(text=str(KTEMP))
            self.ftemplabel.config(text=str(FTEMP))
        except:
            self.ctemplabel.config(text='')
            self.ktemplabel.config(text='')
            self.ftemplabel.config(text='')


if __name__ == "__main__":
    win = App()
    win.geometry("870x500")
    win.title("Convert temperature")
    win.mainloop()