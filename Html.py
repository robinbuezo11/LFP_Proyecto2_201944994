import math

class Html:
    def __init__(self, errors=[], tokens=[]) -> None:
        self.__errors = errors
        self.__tokens = tokens

    def getErrors(self):
        return self.__errors
    
    def getTokens(self):
        return self.__tokens

    def generateResults(self):

        titlecolor = titlesize = bodycolor = bodysize = descolor = dessize = ''
        text = f'<!DOCTYPE html><html><body><div><font size={titlesize} color={titlecolor}>Generacion Archivo HTML</font></br>'
        text += '</div></body></html>'
        
        file=open('./RESULTADOS_201944994.html','w',encoding='utf-8')
        file.write(text)
        file.close()