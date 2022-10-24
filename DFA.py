
class DFA:
    def __init__(self,text=[]) -> None:
        self.__text = text
        self.__status = 0
        self.__errornum = 1
        self.__tokennum = 1
        self.__errors =[]
        self.__tokens =[]
        self.__row = 1
        self.__column = 1
        self.__lexeme = ''

    def analyze(self, text=[]):
        if text == []:
            text = self.__text

        text = self.__deleteComments(text)

        for line in text:
            self.__status = 0
            self.__column = 1
            for char in line:
                if self.__status == 0:
                    self.__status0(char)
                elif self.__status == 1:
                    self.__status1(char)
                elif self.__status == 2:
                    self.__status2(char)
                elif self.__status == 3:
                    self.__status3(char)
                elif self.__status == 4:
                    self.__status4(char)
                elif self.__status == 5:
                    self.__status5(char)
                elif self.__status == 6:
                    self.__status6(char)
                elif self.__status == 7:
                    self.__status7(char)
                elif self.__status == 8:
                    self.__status8(char)
                elif self.__status == 9:
                    self.__status9(char)
                elif self.__status == 10:
                    self.__status10(char)
                elif self.__status == 11:
                    self.__status11(char)
                elif self.__status == 12:
                    self.__status12(char)
                elif self.__status == 13:
                    self.__status13(char)
                elif self.__status == 14:
                    self.__status14(char)
                elif self.__status == 15:
                    self.__status15(char)
                elif self.__status == 16:
                    self.__status16(char)
                elif self.__status == 17:
                    self.__status17(char)        
                self.__column+=1
            self.__row +=1
            
    def __status0(self, char):
        self.__lexeme = ''
        if char == '<':
            self.__status = 1
            self.__lexeme += char
        elif str.isalpha(char):
            self.__status = 5
            self.__lexeme += char
        elif char == ';':
            self.__status = 6
            self.__lexeme += char
        elif char == '-':
            self.__status = 7
            self.__lexeme += char
        elif char == '.':
            self.__status = 10
            self.__lexeme += char
        elif char == '(':
            self.__status = 11
            self.__lexeme += char
        elif char == ')':
            self.__status = 12
            self.__lexeme += char
        elif str.isdigit(char):
            self.__status = 13
            self.__lexeme += char
        elif char == '"':
            self.__status = 16
            self.__lexeme += char
        elif char == ',':
            self.__status = 17
            self.__lexeme += char
        elif char == ' ' or char == '\n' or char == '\t':
            self.__status = 0
        else: 
            self.__errors.append([self.__errornum,'Léxico',self.__row,self.__column,char,f'Error con caracter {char}'])
            self.__errornum += 1
        

    def __status1(self, char):
        if char == '!':
            self.__lexeme += char
            self.__status = 2
        else:
            self.__status = 0
            self.__errors.append([self.__errornum,'Léxico',self.__row,self.__column,char,f'Error con caracter {char}'])
            self.__errornum += 1
            self.__status0(char)

    def __status2(self, char):
        if char == '-':
            self.__lexeme += char
            self.__status = 3
        else:
            self.__status = 0
            self.__errors.append([self.__errornum,'Léxico',self.__row,self.__column,char,f'Error con caracter {char}'])
            self.__errornum += 1
            self.__status0(char)

    def __status3(self, char):
        if char == '-':
            self.__lexeme += char
            self.__status = 4
        else:
            self.__status = 0
            self.__errors.append([self.__errornum,'Léxico',self.__row,self.__column,char,f'Error con caracter {char}'])
            self.__errornum += 1
            self.__status0(char)

    def __status4(self, char):
        self.__tokens.append([self.__tokennum,'Apertura',1,self.__lexeme,self.__row, self.__column])
        self.__tokennum += 1
        self.__status0(char)

    def __status5(self, char):
        if str.isalpha(char) or str.isdigit(char):
            self.__lexeme += char
        else:
            if self.__lexeme == 'Controles':
                self.__tokens.append([self.__tokennum,'Controles',11,self.__lexeme,self.__row, self.__column])
            elif self.__lexeme in ['Contenedor','Boton','Clave','Etiqueta','Texto','Check','RadioBoton','AreaTexto']:
                self.__tokens.append([self.__tokennum,'Control',12,self.__lexeme,self.__row, self.__column])
            elif self.__lexeme == 'Propiedades':
                self.__tokens.append([self.__tokennum,'Propiedades',13,self.__lexeme,self.__row, self.__column])
            elif self.__lexeme == 'Colocacion':
                self.__tokens.append([self.__tokennum,'Colocacion',14,self.__lexeme,self.__row, self.__column])
            else:
                self.__tokens.append([self.__tokennum,'ID',2,self.__lexeme,self.__row, self.__column])
            self.__tokennum += 1
            self.__status0(char)

    def __status6(self, char):
        self.__tokens.append([self.__tokennum,'PuntoComa',3,self.__lexeme,self.__row, self.__column])
        self.__tokennum += 1
        self.__status0(char)

    def __status7(self, char):
        if char == '-':
            self.__lexeme += char
            self.__status = 8
        else:
            self.__status = 0
            self.__errors.append([self.__errornum,'Léxico',self.__row,self.__column,char,f'Error con caracter {char}'])
            self.__errornum += 1
            self.__status0(char)

    def __status8(self, char):
        if char == '>':
            self.__lexeme += char
            self.__status = 9
        else:
            self.__status = 0
            self.__errors.append([self.__errornum,'Léxico',self.__row,self.__column,char,f'Error con caracter {char}'])
            self.__errornum += 1
            self.__status0(char)

    def __status9(self, char):
        self.__tokens.append([self.__tokennum,'Cierre',4,self.__lexeme,self.__row, self.__column])
        self.__tokennum += 1
        self.__status0(char)

    def __status10(self, char):
        self.__tokens.append([self.__tokennum,'Punto',5,self.__lexeme,self.__row, self.__column])
        self.__tokennum += 1
        self.__status0(char)

    def __status11(self, char):
        self.__tokens.append([self.__tokennum,'ParentesisA',6,self.__lexeme,self.__row, self.__column])
        self.__tokennum += 1
        self.__status0(char)

    def __status12(self, char):
        self.__tokens.append([self.__tokennum,'ParentesisC',7,self.__lexeme,self.__row, self.__column])
        self.__tokennum += 1
        self.__status0(char) 

    def __status13(self, char):
        if str.isdigit(char):
            self.__lexeme += char
        elif char == '.':
            self.__lexeme += char
            self.__status = 14
        else:
            self.__tokens.append([self.__tokennum,'Numero',8,self.__lexeme,self.__row, self.__column])
            self.__status0(char)

    def __status14(self, char):
        if str.isdigit(char):
            self.__lexeme += char
            self.__status = 15
        else:
            self.__status = 0
            self.__errors.append([char,self.__row,self.__column])
            self.__status0(char)    

    def __status15(self, char):
        if str.isdigit(char):
            self.__lexeme += char
        else:
            self.__tokens.append([self.__tokennum,'Numero',8,self.__lexeme,self.__row, self.__column])
            self.__status0(char)         

    def __status16(self, char):
        self.__tokens.append([self.__tokennum,'Comilla',9,self.__lexeme,self.__row, self.__column])
        self.__tokennum += 1
        self.__status0(char)    

    def __status17(self, char):
        self.__tokens.append([self.__tokennum,'Coma',10,self.__lexeme,self.__row, self.__column])
        self.__tokennum += 1
        self.__status0(char)   

    def __deleteComments(self,text):
        comment = False
        finaltext = []
        for line in text:
            newline = ''
            if '//' in line:
                line = line[:line.find('//')] + '\n'
            lenline = len(line)+1
            i = 1
            while i < lenline:
                if line[i-1]=='/' and line[i]=='*':
                    comment = True
                if line[i-1]=='*' and line[i]=='/' and comment == True:
                    comment = False
                    i+=2
                else: 
                    if not comment:
                        newline += line[i-1]
                    i+=1
            finaltext.append(newline)
        return finaltext

    def getText(self):
        return self.__text

    def setText(self, text):
        self.__text = text

    def getErrors(self):
        return self.__errors

    def getTokens(self):
        return self.__tokens