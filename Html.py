import math

class Html:
    def __init__(self, errors=[], tokens=[]) -> None:
        self.__errors = errors
        self.__tokens = tokens

    def getErrors(self):
        return self.__errors
    
    def getTokens(self):
        return self.__tokens

    def generateResultsHTML(self):
        operations = self.__operations()

        titlecolor = titlesize = bodycolor = bodysize = descolor = dessize = ''
        for operation in operations:
            if operation[0] == 'Titulo':
                titlecolor = operation[1]
                titlesize = operation[2]
            elif operation[0] == 'Descripcion':
                descolor = operation[1]
                dessize = operation[2]
            elif operation[0] == 'Contenido':
                bodycolor = operation[1]
                bodysize = operation[2]

        text = f'<!DOCTYPE html><html><body><div><font size={titlesize} color={titlecolor}>Generacion Archivo HTML</font></br>'
        for operation in operations:
            if not (operation[0] == 'Titulo' or operation[0] == 'Descripcion' or operation[0] == 'Contenido'):
                text += f'<font size={dessize} color={descolor}>Operacion {operation[0]}:</font></br>'
                text += f'<font size={bodysize} color={bodycolor}>{operation[1]}{operation[2]}</font></br></br>'
        text += '</div></body></html>'
        
        file=open('./RESULTADOS_201944994.html','w',encoding='utf-8')
        file.write(text)
        file.close()