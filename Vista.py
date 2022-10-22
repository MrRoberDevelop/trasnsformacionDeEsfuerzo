import tkinter
import pandas as pd
import sys

from datajson import *
from tkinter import *
from tkinter.ttk import *

class Vista:
    def __init__(self):
        ## inicializar la pantalla de tkinter
        self.master = Tk()
        self.screen=self.master.geometry("1228x720")

        ## agregamos el titulo
        title = Label(self.master, 
                      text="Transformada de esfuerzo plano",
                      font="times 20")
        firstName = Label(self.master,
                      text="Felipe Algarra Alvarez COD. 30000062245")

        title.pack(pady = 10)
        firstName.pack(pady =10)
        self.createTable()
        self.button()



        self.master.mainloop()

    def createTable(self):
        txt = Text(self.master)
        txt.pack()

        class PrintToTXT(object):
            def write(self,s):
                txt.insert(END,s)

            def flush(self):
                pass
        sys.stdout = PrintToTXT()

    def print_data(self):
        df = pd.DataFrame(data=create_data_table())
        print(df)

    def button(self):
        btn = Button(
                self.master,
                text="timbre aqui",
                command = self.print_data
                )
        btn.pack(pady=10)



if __name__ == "__main__":
    vista = Vista()
