import tkinter
import pandas as pd
import sys
import datajson as dj
from datajson import *
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import *
import tkinter.messagebox as tkm
from tkinter import messagebox
import numpy as np
from numpy import *

class Vista:
    def __init__(self):
        ## inicializar la pantalla de tkinter
        self.master = Tk()
        self.master.title('Transformación de esfuerzo plano')
        self.screen=self.master.geometry("1228x720")

        ## agregamos el titulo
        title = Label(self.master, 
                      text="Transformación de esfuerzo plano",
                      font="times 30")
        firstName = Label(self.master,
                      text="Felipe Algarra Álvarez - Código 30000062245", font='times 15 italic')
        secondName = Label(self.master,
                      text="Valeria Mosquera Marín - Código 30000060813", font='times 15 italic')

        title.pack(pady = 10)
        secondName.pack()
        firstName.pack()
        self.createTable()
        self.print_data()
        self.entries()
        self.button()
         
        self.master.mainloop()

    def clear(self):
        self.resultado1.config(text="")
        self.resultado2.config(text="")
        self.resultado3.config(text="")
        self.resultado4.config(text="")
        self.resultado5.config(text="")
        self.resultado6.config(text="")
        self.resultado7.config(text="")
        self.resultado8.config(text="")
        self.resultado9.config(text="")

    def SetText(self, result):
        self.resultado1.config(text=result[0])
        self.resultado2.config(text=result[1])
        self.resultado3.config(text=result[2])
        self.resultado4.config(text=result[3])
        self.resultado5.config(text=result[4])
        self.resultado6.config(text=result[5])
        self.resultado7.config(text=result[6])
        self.resultado8.config(text="")
        self.resultado9.config(text="")

    def calculos(self, sigma_x, sigma_y, Tau_xy, theta):
        self.sigma_xprima = (sigma_x+sigma_y)/2+(sigma_x-sigma_y)/2*cos(2*theta)-Tau_xy*sin(2*theta)
        self.sigma_yprima = (sigma_x + sigma_y) / 2 - (sigma_x - sigma_y) / 2 * cos(2 * theta) + Tau_xy * sin(2 * theta)
        self.Tau_xyprima = (sigma_x - sigma_y) / 2 * sin(2 * theta) + Tau_xy * cos(2 * theta)
        Angulo = arange(0, 181, 1)
        Angulo_rad = radians(Angulo)
        self.sigma_xp = (sigma_x + sigma_y) / 2 + (sigma_x - sigma_y) / 2 * cos(2*Angulo_rad) - Tau_xy * sin(2*Angulo_rad)
        self.Tau_xyp = (sigma_x - sigma_y) / 2 * sin(2 * Angulo_rad) + Tau_xy * cos(2*Angulo_rad)
        self.theta_p = 1 / 2 * np.arctan(-(2 * Tau_xy) / (sigma_x - sigma_y))
        self.sigma_xprin = (sigma_x + sigma_y) / 2 + (sigma_x - sigma_y) / 2 * cos(2 * self.theta_p) - Tau_xy * sin(2 * self.theta_p)
        self.sigma_yprin = (sigma_x + sigma_y) / 2 - (sigma_x - sigma_y) / 2 * cos(2 * self.theta_p) + Tau_xy * sin(2 * self.theta_p)
        self.Tau_xyprin = (sigma_x - sigma_y) / 2 * sin(2 * self.theta_p) + Tau_xy * cos(2 * self.theta_p)
        return self.sigma_xprima, self.sigma_yprima, self.Tau_xyprima, self.theta_p, self.sigma_xprin, self.sigma_yprin, self.Tau_xyprin

    def analisis(self):

        # se obtienen los valores del material

        propMaterial = get_one_item_from_json(self.materialbox.get())

        print(propMaterial)

        self.sigma_x = float(self.Sigmax.get())
        self.sigma_y = float(self.sigmay.get())
        self.Tau_xy = float(self.tauxy.get())
        self.theta = radians(float(self.angulo.get()))
        self.analisis1(self.sigma_x, self.sigma_y, self.Tau_xy, self.theta)

    def analisis1(self, sigma_x, sigma_y, Tau_xy, theta):
        self.clear()
        sol = self.calculos(sigma_x, sigma_y, Tau_xy, theta)
        self.SetText(sol)
        return

    def NewWindow(self):
        self.NWindow = Tk()
        self.NWindow.title('Simulación')
        self.NWindow.geometry("1228x720")
        self.simulacion()

    def simulacion(self):
        ingresar = Label(self.NWindow, text='Ingrese los esfuerzos [Pa]', font='times 20')
        sigmax = Label(self.NWindow, text='σ_x =')
        sigmay = Label(self.NWindow, text='σ_y =')
        tauxy = Label(self.NWindow, text='τ_xy =')
        material = Label(self.NWindow, text='Seleccione el Material', font='times 20')
        
        # Se hace una lista desplegable donde se podra seleccionar el material deseado
        self.materialbox = ttk.Combobox(
            self.NWindow,
            state="readonly",
            values = list_materials()
        )

        # Se setea al primer valor
        self.materialbox.current(0)

        resultados = Label(self.NWindow, text='Resultados', font='times 20')
        angulo = Label(self.NWindow, text='Ingrese el ángulo de rotación', font='times 20')
        theta = Label(self.NWindow, text='θ =')
        self.Sigmax = Entry(self.NWindow)
        self.sigmay = Entry(self.NWindow)
        self.tauxy = Entry(self.NWindow)
        self.angulo = Entry(self.NWindow)
        self.Sigmax.place(x=100, y=80)
        self.sigmay.place(x=100, y=130)
        self.tauxy.place(x=100, y=180)
        self.angulo.place(x=570, y=80)
        R_sigmax = Label(self.NWindow, text="σ_x' para el ángulo dado = ", font='times 15')
        R_sigmay = Label(self.NWindow, text="σ_y' para el ángulo dado = ", font='times 15')
        R_tau = Label(self.NWindow, text="τ_xy' para el ángulo dado = ", font='times 15')
        angle = Label(self.NWindow, text="Ángulo para esfuerzos máximos = ", font='times 15')
        sigma_xprincipal = Label(self.NWindow, text="σ_x principal = ", font='times 15')
        sigma_yprincipal = Label(self.NWindow, text="σ_y principal = ", font='times 15')
        tau_principal = Label(self.NWindow, text="τ_xy principal = ", font='times 15')
        FS_tresca = Label(self.NWindow, text="Factor de seguridad Tresca = ", font='times 15')
        FS_mises = Label(self.NWindow, text="Factor de seguridad Von Mises = ", font='times 15')
        self.resultados = Button(self.NWindow, text='Iniciar simulación', command=self.analisis)
        self.resultados.place(x=600, y=230)
        self.resultado1 = Label(self.NWindow, text="", font="times 15")
        self.resultado2 = Label(self.NWindow, text="", font="times 15")
        self.resultado3 = Label(self.NWindow, text="", font="times 15")
        self.resultado4 = Label(self.NWindow, text="", font="times 15")
        self.resultado5 = Label(self.NWindow, text="", font="times 15")
        self.resultado6 = Label(self.NWindow, text="", font="times 15")
        self.resultado7 = Label(self.NWindow, text="", font="times 15")
        self.resultado8 = Label(self.NWindow, text="", font="times 15")
        self.resultado9 = Label(self.NWindow, text="", font="times 15")
        ingresar.place(x=60,y=30)
        material.place(x=900, y=30)
        self.materialbox.place(x=900, y=80)
        sigmax.place(x=60,y=80)
        sigmay.place(x=60,y=130)
        tauxy.place(x=60,y=180)
        resultados.place(x=60,y=250)
        angulo.place(x=500, y=30)
        theta.place(x=530, y=80)
        R_sigmax.place(x=60, y=300)
        R_sigmay.place(x=60, y=330)
        R_tau.place(x=60, y=360)
        angle.place(x=60, y=390)
        sigma_xprincipal.place(x=60, y=420)
        sigma_yprincipal.place(x=60, y=450)
        tau_principal.place(x=60, y=480)
        FS_tresca.place(x=60, y=510)
        FS_mises.place(x=60, y=540)
        self.resultado1.place(x=300, y=300)
        self.resultado2.place(x=300, y=330)
        self.resultado3.place(x=300, y=360)
        self.resultado4.place(x=350, y=390)
        self.resultado5.place(x=200, y=420)
        self.resultado6.place(x=200, y=450)
        self.resultado7.place(x=200, y=480)
        self.resultado8.place(x=500, y=510)
        self.resultado9.place(x=500, y=540)

    def entries(self):
        self.frame = Frame(self.master)
        self.frame.pack()

        lista = [
            "Material",
            "Tipo",
            "Densidad",
            "Esfuerzo de fluencia",
            "Módulo"
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
                                text="Nuevo material",
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
        self.removeValues.grid(row=2,column=3)


    def delete(self):
        data = get_one_item_from_json(self.material.get())
        if data is not None:
            delete_item(self.material.get())
            self.print_data()
            self.clean_spaces()
        else:
            messagebox.showerror(
                "Elemento inexistente",
                "El material que intenta borrar no se encuentra disponible"
            )


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
                text="Realizar Simulación",
                command = self.NewWindow
                )
        btn.place(x=1000, y=650)



if __name__ == "__main__":
    vista = Vista()
