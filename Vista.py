import tkinter
import pandas as pd
import sys


from datajson import *
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

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
        self.print_data()
        self.entries()
         
        self.master.mainloop()


    def entries(self):
        self.frame = Frame(self.master)
        self.frame.pack()

        lista = [
            "material",
            "tipo",
            "densidad",
            "esfuerzo",
            "modulo"
        ]

        for i in range(len(lista)):
            l=Label(self.frame,text=lista[i])
            l.grid(row=0,column=i)

        self.material  = Entry(self.frame)
        self.tipo = Entry(self.frame)
        self.densidad = Entry(self.frame)
        self.esfuerzo = Entry(self.frame)
        self.modulo = Entry(self.frame)
        self.addValues = Button(self.frame,
                                text="nuevo material",
                                command=self.nuevo)
        self.removeValues = Button(self.frame,
                                text="Eliminar material",
                                command=self.delete)

        self.material.grid(row=1, column=0)
        self.tipo.grid(row=1, column=1)
        self.densidad.grid(row=1, column=2)
        self.esfuerzo.grid(row=1, column=3)
        self.modulo.grid(row=1, column=4)

        self.addValues.grid(row=2,column=1)
        self.removeValues.grid(row=2,column=2)


    def delete(self):
        delete_item(self.material.get())
        self.print_data()
        self.clean_spaces()


    def nuevo(self):
        data = get_one_item_from_json(self.material.get())
        if data is not None:
            #print(data)
            messagebox.showerror(
                "Elemento existente",
                "El material ya se encuentra en nuestra base de datos por favor revisar los datos de entrada"
            )
        else:
            #print("nothing")
            try:
                if self.material.get() != "" and self.tipo.get() !="":
                    material={
                        "name"  :self.material.get(),
                        "tipo"      :self.tipo.get(),
                        "desidad"   :float(self.densidad.get()),
                        "esfuerzo"  :float(self.esfuerzo.get()),
                        "modulo"    :float(self.modulo.get())
                    }
                    include_data(material)
                    self.print_data()
                else:
                    messagebox.showerror(
                        "Error de datos",
                        "El material necesita un nombre y un tipo"
                    )
            except:
                messagebox.showerror(
                    "Error de datos",
                    "Los datos no corresponden a valores validos.\n" + 
                    "Por favor reingresa los datos."
                )
            finally:
                self.clean_spaces()
    def clean_spaces(self):
        self.material.delete(0,'end')
        self.tipo.delete(0,'end')
        self.densidad.delete(0,'end')
        self.esfuerzo.delete(0,'end')
        self.modulo.delete(0,'end')


    def createTable(self):
        txt = Text(self.master)
        txt.pack()

        class PrintToTXT(object):
            def flush(self):
                pass
            def write(self,s):
                txt.insert("1.0",s)
        sys.stdout = PrintToTXT()


    def print_data(self):
        df = pd.DataFrame(data=create_data_table())
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
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
