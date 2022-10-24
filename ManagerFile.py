from tkinter import messagebox as msgbx
from tkinter.filedialog import askopenfilename, asksaveasfile

from DFA import DFA
from PDA import PDA

class ManagerFile:
    def __init__(self) -> None:
        self.__path = None
        self.__data = []

    #----------------------- Functions ----------------------------
    def openFile(self):   #Metodo para leer el archivo
        try:
            path = askopenfilename(title='Abrir',defaultextension='.gpw',filetypes=[('GPW','*.gpw'),('All Filles','*')])
            file = open(path,'r',encoding='utf-8')
            self.__path = path
            if file is not None:
                self.__data = file.readlines()
                file.close()
            msgbx.showinfo('Archivo Cargado','El archivo se cargó exitosamente')
        except Exception:
            if file is not None:
                file.close()
            msgbx.showerror("ERROR",'Error en la carga, revise que los datos y la ruta de su archivo sean correctos.')

    def analyzeText(self,text=None):     #Metodo para analizar el archivo
        dfa = DFA()
        text = text.split('\n')
        iterator = 0
        if text is None:
            dfa.analyze(self.__data)
        else:
            for line in text:
                text[iterator] = line + '\n'
                iterator += 1
            dfa.analyze(text)
        #print(dfa.getErrors())
        #print('----------------------------------------------------')
        #print(dfa.getTokens())
        if len(dfa.getTokens()) != 0:
            pda=PDA(dfa.getErrors(),dfa.getTokens())
            pda.analyze()
            return (pda.getErrors(),pda.getTokens())
        else:
            return (dfa.getErrors(),dfa.getTokens())

    def save(self,data,saveas=False):
        try:
            if saveas:
                file = asksaveasfile(title='Guardar como',defaultextension='.txt',filetypes=[('Todos','*.*')],mode='w')
            else:
                if self.__path:
                    file = open(self.__path,'w', encoding='utf-8')
                else:
                    file = asksaveasfile(title='Guardar como',defaultextension='.txt',filetypes=[('Todos','*.*')],mode='w')
            if file is not None:
                file.write(data)
                file.close()
                msgbx.showinfo('Guardado','Archivo guardado exitosamente')
            else:
                msgbx.showerror('Error','No se ha seleccionado ningún archivo')
        except Exception as e:
            if file is not None:
                file.close()
            msgbx.showerror("ERROR",e)

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def getPath(self):
        return self.__path

    def setPath(self, path):
        self.__path = path


