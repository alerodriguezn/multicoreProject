from tkinter import *
from pandastable import Table, TableModel
import pandas as pd

def desplegarGUI():
    class GUIdatos(Frame):
            def __init__(self, parent=None):
                self.parent = parent
                Frame.__init__(self)
                self.main = self.master
                self.main.geometry('600x400+200+100')
                self.main.title('Resultados')
                f = Frame(self.main)
                f.pack(fill=BOTH,expand=1)
                df = pd.read_csv('multicoreProject/datos.csv',encoding='latin-1')
                self.table = pt = Table(f, dataframe=df,
                                        showtoolbar=True, showstatusbar=True)
                pt.show()
                return

    app = GUIdatos()
    app.mainloop()