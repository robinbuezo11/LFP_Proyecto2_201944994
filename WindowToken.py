import tkinter as tk

class WindowToken(tk.Toplevel):
    def __init__(self, master, tokens=[]) -> None:
        super().__init__(master)
        self.title("Tokens")
        self.geometry('500x405')
        self.resizable(False,False)

        #----------------------------- Table Tokens-----------------------------

        columns = ('No.','Token','Numero','Lexema')
        self.__tokenstable = tk.ttk.Treeview(self,columns=columns,show='headings')

        iter = 1
        while iter < 5:
            if iter == 1 or iter == 3:
                self.__tokenstable.column(f'#{iter}', width=60, anchor='center')
                self.__tokenstable.heading(f'#{iter}', text=columns[iter-1])
            else:
                self.__tokenstable.column(f'#{iter}', width=190 ,anchor='center')
                self.__tokenstable.heading(f'#{iter}', text=columns[iter-1])
            iter += 1
        self.__tokenstable.place(x=10,y= 10,width=473,height=386)

        #----------------------------- Scroll Tokens -----------------------------
        
        self.__scrolltokens = tk.Scrollbar(self, command=self.__tokenstable.yview)
        self.__tokenstable.config(yscrollcommand=self.__scrolltokens.set)
        self.__scrolltokens.place(x=483, y=10, height=386)

        self.focus()
        self.transient(self.master)
        self.grab_set()

        self.__settokensvalues(tokens)

    def __settokensvalues(self, tokens):
        self.__tokenstable.delete(*self.__tokenstable.get_children())
        if len(tokens) != 0:
            for token in tokens:
                self.__tokenstable.insert('',tk.END,values=token)  
        else:
            tk.messagebox.showwarning('Vacío','No hay ningún dato')