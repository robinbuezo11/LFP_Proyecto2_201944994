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
        self.__generateHTML()
        self.__generateCSS()

    def __generateHTML(self):

        body = ''
        components = []

        text = f'<!DOCTYPE html><html><head><title>LFPA+ - Proyecto 2</title><link href="/Resultados/style.css" rel="stylesheet" type="text/css"/></head><body><h1>Prueba</h1></body></html>'
        file=open('Resultados/index.html','w',encoding='utf-8')
        file.write(text)
        file.close()

    def __generateCSS(self):
        text = 'h1{'+'color: rgb(20, 75, 200);}'
        file=open('Resultados/style.css','w',encoding='utf-8')
        file.write(text)
        file.close()