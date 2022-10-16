import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbx
from ManagerFile import ManagerFile
from Html import Html

class WindowMain(ttk.Frame):
    def __init__(self, master, mfile=ManagerFile()) -> None:
        super().__init__(master)
        master.title('Proyecto 2')
        master.geometry('800x700')
        master.config(background='sky blue')
        master.resizable(False,False)
        self.__mfile = mfile
        self.__html = Html()

        #----------------------------- Menu -----------------------------

        self.__menu = tk.Menu()

        self.__menufile = tk.Menu(self.__menu, tearoff=False)
        self.__menu.add_cascade(menu=self.__menufile, label='Archivo')

        self.__menufile.add_command(label='Nuevo', command=self.__new)
        self.__menufile.add_command(label='Abrir', command=self.__open)
        self.__menufile.add_command(label='Guardar', command=self.__save)
        self.__menufile.add_command(label='Guardar Como', command=self.__saveAs)
        self.__menufile.add_command(label='Salir', command=self.__exit)

        self.__menuanalyze = tk.Menu(self.__menu, tearoff=False)
        self.__menu.add_cascade(menu=self.__menuanalyze, label='Análisis')

        self.__menuanalyze.add_command(label='Generar página web', command=self.__generate)

        self.__menutoken = tk.Menu(self.__menu, tearoff=False)
        self.__menu.add_cascade(menu=self.__menutoken, label='Tokens')

        self.__menutoken.add_command(label='Ver Tokens', command=self.__tokens)

        self.__menuhelp = tk.Menu(self.__menu, tearoff=False)
        self.__menu.add_cascade(menu=self.__menuhelp, label='Ayuda')

        self.__menuhelp.add_command(label='Manual Técnico', command=self.__tecmanual)
        self.__menuhelp.add_command(label='Manual de Usuario', command=self.__usermanual)
        self.__menuhelp.add_command(label='Temas de Ayuda', command=self.__help)

        master.config(menu=self.__menu)

        #----------------------------- Entry Text -----------------------------

        self.__entrytext = tk.Text(master=master)
        self.__entrytext.place(relwidth=1, height=525)
        self.__entrytext.bind('<KeyRelease>', self.__position)
        self.__entrytext.bind('<ButtonRelease>', self.__position)

        #----------------------------- Label Position-----------------------------

        self.__infomsg = tk.StringVar(value='Editor de texto')
        self.__infolbl = tk.Label(master, textvariable=self.__infomsg, anchor='e')
        self.__infolbl.place(y=525, relwidth=1)

        #----------------------------- Table Errors-----------------------------

        columns = ('No.','Tipo','Linea','Columna','Lexema/Token','Descripción')
        self.__errorstable = ttk.Treeview(master,columns=columns,show='headings')

        iter = 1
        while iter < 7:
            if iter == 1:
                self.__errorstable.column(f'#{iter}', width=30, anchor='center')
                self.__errorstable.heading(f'#{iter}', text=columns[iter-1])
            elif iter == 2:
                self.__errorstable.column(f'#{iter}', width=130, anchor='center')
                self.__errorstable.heading(f'#{iter}', text=columns[iter-1])
            elif iter == 6:
                self.__errorstable.column(f'#{iter}', width=300)
                self.__errorstable.heading(f'#{iter}', text=columns[iter-1])
            else:
                self.__errorstable.column(f'#{iter}', width=100 ,anchor='center')
                self.__errorstable.heading(f'#{iter}', text=columns[iter-1])
            iter += 1
        self.__errorstable.place(y=550,relwidth=1,relheight=0.2)

    def __position(self, event=None): 
        pos = self.__entrytext.index(tk.INSERT)
        pos = pos.split('.')
        self.__infomsg.set(f'Línea: {pos[0]}\tColumna: {pos[1]}')

    def __new(self):
        try:
            if self.__entrytext.get(1.0,'end-1c') == '':
                self.__entrytext.delete(1.0,'end')
            else:
                if msgbx.askyesno('Guardar', '¿Desea guardar el archivo?'):
                    self.__mfile.save(self.__entrytext.get(1.0,'end-1c'))
                self.__entrytext.delete(1.0,'end')
            self.__position()
        except Exception as e:
                    msgbx.showerror('Error',e)
        

    def __open(self):
        try:
            self.__new()
            self.__mfile.openFile()
            self.__entrytext.delete(1.0,'end')
            for line in self.__mfile.getData():
                self.__entrytext.insert('end', line)
            self.__position()
        except Exception as e:
            msgbx.showerror('Error',e)

    def __save(self):
        try:
            self.__mfile.save(self.__entrytext.get(1.0,'end-1c'))
        except Exception as e:
            msgbx.showerror('Error',e)

    def __saveAs(self):
        try:
            self.__mfile.save(self.__entrytext.get(1.0,'end-1c'),True)
        except Exception as e:
            msgbx.showerror('Error',e)
    
    def __generate(self):
        try:
            (errors,tokens) = self.__mfile.analyzeText(self.__entrytext.get(1.0,'end-1c'))
            self.__html = Html(errors=errors,tokens=tokens)
            if len(errors) == 0 and len(tokens) != 0:
                self.__html.generateResults()
                self.__errorstable.delete(*self.__errorstable.get_children())
                msgbx.showinfo('Archivo Analizado','El archivo se analizó correctamente, se ha generado la página web')
            elif len(tokens) == 0:
                msgbx.showinfo('Texto vacío', 'Debe ingresar el texto para poder generar la página web')
            else:
                self.__seterrorsvalues(errors)
                msgbx.showerror('Error en Análisis','Se encontraron errores en el análisis, por favor revise')
        except Exception as e:
            msgbx.showerror('Error',e) 

    def __tokens(self):
        msgbx.showinfo(message='Boton Tokens')

    def __usermanual(self):
        subprocess.Popen(["Documentación\Manual de Usuario.pdf"], shell=True)

    def __tecmanual(self):
        subprocess.Popen(["Documentación\Manual Técnico.pdf"], shell=True)

    def __help(self):
        msgbx.showinfo('Ayuda','Desarrollador: Robin Omar Buezo Díaz\nCarne: 201944994\nCurso: Lenguajes Formales y De Programacion')

    def __exit(self):
        self.master.destroy()

    def __seterrorsvalues(self, errors):
        self.__errorstable.delete(*self.__errorstable.get_children())
        if len(errors) != 0:
            for error in errors:
                self.__errorstable.insert('',tk.END,values=error)  
        else:
            msgbx.showwarning('Vacío','No hay ningún dato')

