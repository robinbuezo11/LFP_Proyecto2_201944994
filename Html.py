import math

class Html:
    def __init__(self, errors=[], tokens=[]) -> None:
        self.__errors = errors
        self.__tokens = tokens
        self.__components = []

    def getErrors(self):
        return self.__errors
    
    def getTokens(self):
        return self.__tokens

    def generateResults(self):
        self.__generateHTML()
        self.__generateCSS()

    def __generateHTML(self):

        self.__generateComponents()

        body = ''

        text = f'<!DOCTYPE html><html><head><title>LFPA+ - Proyecto 2</title><link href="/Resultados/style.css" rel="stylesheet" type="text/css"/></head><body><h1>Prueba</h1></body></html>'
        file=open('Resultados/index.html','w',encoding='utf-8')
        file.write(text)
        file.close()

    def __generateCSS(self):
        text = 'h1{'+'color: rgb(20, 75, 200);}'
        file=open('Resultados/style.css','w',encoding='utf-8')
        file.write(text)
        file.close()

    def __generateComponents(self):
        self.__components = []

        i=0
        for token in self.__tokens:
            try:
                if token[2] == 12 and self.__tokens[i+1][2] == 2 and self.__tokens[i+2][2] == 3:
                    self.__components.append([token[2],token[1],self.__tokens[i+1][3]],None,None,None,None,None,None,None,None)
                elif token[2] == 2 and self.__tokens[i+1][2] == 5 and self.__tokens[i+2][2] == 2 and self.__tokens[i+3][2] == 6:
                    if self.__tokens[i+2][3] == 'setColorLetra':
                        component = self.__searchComponentById(token[3])
                        j=i+4
                        numlist = []
                        while self.__components[j][2] == 8:
                            numlist.append(self.__components[j][3])
                            j+=2  
                        component[3] = numlist
                        self.__setComponentById(component[2],component)
                    elif self.__tokens[i+2][3] == 'setTexto':
                        component = self.__searchComponentById(token[3])
                        if self.__tokens[i+4][2] == 9 and self.__tokens[i+5][2] == 2:
                            component[4] = self.__tokens[i+5][3]
                            self.__setComponentById(component[2],component)
                    elif self.__tokens[i+2][3] == 'setAlineacion':
                        component = self.__searchComponentById(token[3])
                        if self.__tokens[i+4][3] in ['Centro','Izquierdo','Derecho']:
                            component[6] = self.__tokens[i+4][3]
                        else:
                            component[6] = 'Izquierdo'
                        self.__setComponentById(component[2],component)
                    elif self.__tokens[i+2][3] == 'setColorFondo':
                        component = self.__searchComponentById(token[3])
                        j=i+4
                        numlist = []
                        while self.__components[j][2] == 8:
                            numlist.append(self.__components[j][3])
                            j+=2  
                        component[5] = numlist
                        self.__setComponentById(component[2],component)
                    elif self.__tokens[i+2][3] == 'setMarcada':
                        component = self.__searchComponentById(token[3])
                        if self.__tokens[i+4][3] == 'True':
                            component[7] = self.__tokens[i+4][3]
                        else:
                            component[7] = 'False'
                        self.__setComponentById(component[2],component)
                    elif self.__tokens[i+2][3] == 'setGrupo':
                        component = self.__searchComponentById(token[3])
                        if self.__tokens[i+4][2] == 2:
                            id = self.__searchComponentById(self.__tokens[i+4][3])
                            if id is not None:
                                component[8] = self.__tokens[i+4][3]
                        self.__setComponentById(component[2],component)
            except:
                pass

            i+=1
        return self.__components

    def __searchComponentById(self, id):
        for component in self.__components:
            if component[2] == id:
                return component

    def __setComponentById(self, id, newcomponent):
        i=0
        for component in self.__components:
            if component[2] == id:
                self.__components[i] = newcomponent
            i+=1