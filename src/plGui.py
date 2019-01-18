from tkinter import *
from tkinter import ttk
from practicasLaboralesList import practicasLaboralesList
from practicaLaboral import practicaLaboral
class plGui:

    def __init__(self, path):

        self.pllista=practicasLaboralesList(path)

        self.gui = Tk()
        self.gui.title("Buscador de practicas laborales - ITBA - GEDA")
        self.currEstate = "empresa"
        self.lbContent=[]
        self.frameSup = Frame(self.gui)
        self.frameSup.pack(side=TOP,fill=BOTH, expand=True)

        self.frameInf = Frame(self.gui)
        self.frameInf.pack(side=BOTTOM,fill=BOTH, expand=True)

        self.titulo = ttk.Label(self.frameSup, text="Dpartamento de ingenieria electronica - informe de practica laboral")
        self.srcollBar = Scrollbar(self.frameInf)
        self.empresab = ttk.Button(self.frameSup, text="Empresa", command=self.empresa)
        self.tagsb = ttk.Button(self.frameSup, text="Tags", command=self.tags)
        self.anb = ttk.Button(self.frameSup, text="Apellido y Nombre", command=self.ayn)
        self.textbbuscar = StringVar()
        self.buscarb = ttk.Button(self.frameInf, textvariable=self.textbbuscar, command=self.buscar)
        self.textbbuscar.set("Buscar")



        #scrolbar en el list box#
        self.listbox = Listbox(self.frameInf, yscrollcommand=self.srcollBar.set)
        self.srcollBar.config(command=self.listbox.yview)

        #Formato de la gui#
        self.titulo.pack(side=TOP, fill=BOTH, expand=True)
        self.empresab.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.tagsb.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.anb.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.buscarb.pack(side=BOTTOM,fill = X, expand=True, padx=5, pady=5)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)
        self.srcollBar.pack(side=RIGHT, fill= Y, expand=True)


        for i in range(30):
            self.listbox.insert(i + 1,str(i))
            self.listbox.pack()



        self.gui.mainloop()

    def conectar(self):
        print("clock")

    def tags(self):
        tempSet = set()
        tempList = []
        self.textbbuscar.set("Buscar")
        self.buscarb.pack()
        self.listbox.delete(0, END) #borro el contenido del listbox
        self.listbox.config(selectmode=MULTIPLE)
        self.lbContent = self.pllista.listaPracticasLaborales
        for row in self.lbContent:
            for subr in row.tags:
                tempSet.add(str(subr))

        tempList = list(tempSet)
        tempList.sort()
        tempList.reverse()
        for row in tempList:
            i = 0
            self.listbox.insert(i, row)
            i = i + 1


        self.listbox.pack()



    def empresa(self):
        tempSet=set()
        tempList=[]
        self.textbbuscar.set("Buscar")
        self.buscarb.pack()
        self.listbox.delete(0, END)
        self.listbox.config(selectmode=SINGLE)

        self.lbContent=sorted(self.pllista.listaPracticasLaborales, key=lambda practicaLaboral:practicaLaboral.empresa)
        self.lbContent.reverse()
        for row in self.lbContent:
            tempSet.add(row.empresa)
        tempList=list(tempSet)
        tempList.sort()
        tempList.reverse()
        for row in tempList:
            i=0
            self.listbox.insert(i, row)
            i=i+1

        self.listbox.pack()



    def ayn(self):
        self.textbbuscar.set("Abrir")
        self.buscarb.pack()
        self.listbox.delete(0, END)
        self.lbContent = sorted(self.pllista.listaPracticasLaborales,key=lambda practicaLaboral: practicaLaboral.apellido)
        self.lbContent.reverse()
        for row in self.lbContent:
            i=0
            self.listbox.insert(i, row.apellido +" " + row.nombre+"("+str(row.legajo)+")")
            i=i+1
        self.listbox.config(selectmode=SINGLE)

        self.listbox.pack()


    def buscar(self):
        print("buscar")


