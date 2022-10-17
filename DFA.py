
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

        self.__errors =[]
        self.__tokens =[]
        self.__row = 1
        self.__errornum = 1
        self.__tokennum = 1

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
                self.__column+=1
            self.__row +=1
            
    def __status0(self, char):
        self.__lexeme = ''
        if char == '<':
            self.__status = 1
            self.__lexeme += char
        elif str.isalpha(char):
            self.__status = 3
            self.__lexeme += char
        elif char == '=':
            self.__status = 4
            self.__lexeme += char
        elif str.isdigit(char):
            self.__status = 5
            self.__lexeme += char
        elif char == '/':
            self.__status = 6
            self.__lexeme += char
        elif char == ',':
            self.__status = 7
            self.__lexeme += char
        elif char == '.':
            self.__status = 8
            self.__lexeme += char
        elif char == '[':
            self.__status = 9
            self.__lexeme += char
        elif char == ']':
            self.__status = 10
            self.__lexeme += char
        elif char == '>':
            self.__status = 13
            self.__lexeme += char
        elif char == ' ' or char == '\n' or char == '\t':
            self.__status = 0
        else: 
            self.__errors.append([self.__errornum,'Léxico',self.__row,self.__column,char,f'Error con caracter {char}'])
            self.__errornum += 1
        

    def __status1(self, char):
        if char == '/':
            self.__lexeme += char
            self.__status2()
        else:
            self.__tokens.append([self.__tokennum,'Apertura',1,self.__lexeme])
            self.__tokennum += 1
            self.__status0(char)

    def __status2(self):
        self.__tokens.append([self.__tokennum,'Apertura',1,self.__lexeme])
        self.__tokennum += 1
        self.__status = 0

    def __status3(self, char):
        if str.isalpha(char):
            self.__lexeme += char
        else:
            self.__tokens.append([self.__tokennum,'Palabra',2,self.__lexeme])
            self.__tokennum += 1
            self.__status0(char)

    def __status4(self, char):
        self.__tokens.append([self.__tokennum,'Igual',3,self.__lexeme])
        self.__tokennum += 1
        self.__status0(char)

    def __status5(self, char):
        if str.isdigit(char):
            self.__lexeme += char
        elif char == '.':
            self.__lexeme += char
            self.__status = 11
        else:
            self.__tokens.append([self.__tokennum,'Numero',4,self.__lexeme])
            self.__tokennum += 1
            self.__status0(char)

    def __status6(self, char):
        if char == '>':
            self.__lexeme += char
            self.__status = 13
        else:
            self.__status = 0
            self.__errors.append([self.__errornum,'Léxico',self.__row,self.__column,char,f'Error con caracter {char}'])
            self.__errornum += 1
            self.__status0(char)

    def __status7(self, char):
        self.__tokens.append([self.__tokennum,'Coma',5,self.__lexeme])
        self.__tokennum += 1
        self.__status0(char)

    def __status8(self, char):
        self.__tokens.append([self.__tokennum,'Punto',6,self.__lexeme])
        self.__tokennum += 1
        self.__status0(char)

    def __status9(self, char):
        self.__tokens.append([self.__tokennum,'CorcheteA',7,self.__lexeme])
        self.__tokennum += 1
        self.__status0(char)

    def __status10(self, char):
        self.__tokens.append([self.__tokennum,'CorcheteC',8,self.__lexeme])
        self.__tokennum += 1
        self.__status0(char)

    def __status11(self, char):
        if str.isdigit(char):
            self.__lexeme += char
            self.__status = 12
        else:
            self.__status = 0
            self.__errors.append([self.__errornum,'Léxico',self.__row,self.__column,char,f'Error con caracter {char}'])
            self.__errornum += 1
            self.__status0(char)

    def __status12(self, char):
        if str.isdigit(char):
            self.__lexeme += char
        else:
            self.__tokens.append([self.__tokennum,'Numero',4,self.__lexeme])
            self.__tokennum += 1
            self.__status0(char)   

    def __status13(self, char):
        self.__tokens.append([self.__tokennum,'Cierre',9,self.__lexeme])
        self.__tokennum += 1
        self.__status0(char)      

    def getText(self):
        return self.__text

    def setText(self, text):
        self.__text = text

    def getErrors(self):
        return self.__errors

    def getTokens(self):
        return self.__tokens