import math

class Html:
    def __init__(self, errors=[], tokens=[]) -> None:
        self.__errors = errors
        self.__tokens = tokens

    def getErrors(self):
        return self.__errors
    
    def getTokens(self):
        return self.__tokens

    def generateErrorsHTML(self):
        text='<!DOCTYPE html><html><body><div style="text-align:center"><h1>Tabla de Errores</h1>'
        text+='<table border=1 style="margin: 0 auto;" class="default">'
        text+='<tr><th>No.</th><th>Lexema</th><th>Tipo</th><th>Columna</th><th>Fila</th></tr>'
        iterator=0
        for error in self.__errors:
            text+=f'<tr><td>{iterator}</td><td>{error[0]}</td><td>Error</td><td>{error[2]}</td><td>{error[1]}</td></tr>'
            iterator+=1
        text+='</table></div></body></html>'

        file=open('./ERRORES_201944994.html','w',encoding='utf-8')
        file.write(text)
        file.close()

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

    def __operations(self):
        data=[]
        iterator=0
        for line in self.__tokens:
            if line[1] == 'Operacion' and self.__tokens[iterator+2][1]=='SUMA':
                iter=iterator
                operation = ''
                result = 0
                while not (self.__tokens[iter][1] == '</' and self.__tokens[iter+1][1] == 'Operacion'):
                    if self.__tokens[iter][0]=='Numero':
                        if operation == '':
                            operation += self.__tokens[iter][1]
                        else:
                            operation += '+'
                            operation += self.__tokens[iter][1]
                        result += float(self.__tokens[iter][1])
                    iter+=1
                operation += '='
                data.append(['SUMA',operation,result])
            elif line[1] == 'Operacion' and self.__tokens[iterator+2][1]=='RESTA':
                iter=iterator
                operation = ''
                result = 0
                while not (self.__tokens[iter][1] == '</' and self.__tokens[iter+1][1] == 'Operacion'):
                    if self.__tokens[iter][0]=='Numero':
                        if operation == '':
                            operation += self.__tokens[iter][1]
                            result = float(self.__tokens[iter][1])
                        else:
                            operation += '-'
                            operation += self.__tokens[iter][1]
                            result -= float(self.__tokens[iter][1])
                    iter+=1
                operation += '='
                data.append(['RESTA',operation,result])
            elif line[1] == 'Operacion' and self.__tokens[iterator+2][1]=='MULTIPLICACION':
                iter=iterator
                operation = ''
                result = 0
                while not (self.__tokens[iter][1] == '</' and self.__tokens[iter+1][1] == 'Operacion'):
                    if self.__tokens[iter][0]=='Numero':
                        if operation == '':
                            operation += self.__tokens[iter][1]
                            result = float(self.__tokens[iter][1])
                        else:
                            operation += '*'
                            operation += self.__tokens[iter][1]
                            result *= float(self.__tokens[iter][1])
                    iter+=1
                operation += '='
                data.append(['MULTIPLICACION',operation,result])
            elif line[1] == 'Operacion' and self.__tokens[iterator+2][1]=='DIVISION':
                iter=iterator
                operation = ''
                result = 0
                while not (self.__tokens[iter][1] == '</' and self.__tokens[iter+1][1] == 'Operacion'):
                    if self.__tokens[iter][0]=='Numero':
                        if operation == '':
                            operation += self.__tokens[iter][1]
                            result = float(self.__tokens[iter][1])
                        else:
                            operation += '/'
                            operation += self.__tokens[iter][1]
                            result /= float(self.__tokens[iter][1])
                    iter+=1
                operation += '='
                data.append(['DIVISION',operation,result])
            elif line[1] == 'Operacion' and self.__tokens[iterator+2][1]=='POTENCIA':
                iter=iterator
                operation = ''
                result = 0
                while not (self.__tokens[iter][1] == '</' and self.__tokens[iter+1][1] == 'Operacion'):
                    if self.__tokens[iter][0]=='Numero':
                        if operation == '':
                            operation += self.__tokens[iter][1]
                            result = float(self.__tokens[iter][1])
                        else:
                            operation += '^'
                            operation += self.__tokens[iter][1]
                            result **= float(self.__tokens[iter][1])
                    iter+=1
                operation += '='
                data.append(['POTENCIA',operation,result])
            elif line[1] == 'Operacion' and self.__tokens[iterator+2][1]=='RAIZ':
                iter=iterator
                operation = ''
                result = 0
                while not (self.__tokens[iter][1] == '</' and self.__tokens[iter+1][1] == 'Operacion'):
                    if self.__tokens[iter][0]=='Numero':
                        if operation == '':
                            operation += self.__tokens[iter][1]
                            result = 1/float(self.__tokens[iter][1])
                        else:
                            operation += 'r'
                            operation += self.__tokens[iter][1]
                            result **= 1/float(self.__tokens[iter][1])
                    iter+=1
                operation += '='
                data.append(['RAIZ',operation,result])
            elif line[1] == 'Operacion' and self.__tokens[iterator+2][1]=='INVERSO':
                iter=iterator
                operation = ''
                result = 0
                while not (self.__tokens[iter][1] == '</' and self.__tokens[iter+1][1] == 'Operacion'):
                    if self.__tokens[iter][0]=='Numero':
                        if operation == '':
                            operation += 'Inver('
                            operation += self.__tokens[iter][1]
                            result = 1/float(self.__tokens[iter][1])
                        else:
                            operation += 'Inver('
                            operation += self.__tokens[iter][1]
                            result = 1/float(self.__tokens[iter][1])
                    iter+=1
                operation += ')='
                data.append(['INVERSO',operation,result])
            elif line[1] == 'Operacion' and self.__tokens[iterator+2][1]=='SENO':
                iter=iterator
                operation = ''
                result = 0
                while not (self.__tokens[iter][1] == '</' and self.__tokens[iter+1][1] == 'Operacion'):
                    if self.__tokens[iter][0]=='Numero':
                        if operation == '':
                            operation += 'Sen('
                            operation += self.__tokens[iter][1]
                            result = math.sin(float(self.__tokens[iter][1]))
                        else:
                            operation += 'Sen('
                            operation += self.__tokens[iter][1]
                            result = math.sin(float(self.__tokens[iter][1]))
                    iter+=1
                operation += ')='
                data.append(['SENO',operation,result])   
            elif line[1] == 'Operacion' and self.__tokens[iterator+2][1]=='COSENO':
                iter=iterator
                operation = ''
                result = 0
                while not (self.__tokens[iter][1] == '</' and self.__tokens[iter+1][1] == 'Operacion'):
                    if self.__tokens[iter][0]=='Numero':
                        if operation == '':
                            operation += 'Cos('
                            operation += self.__tokens[iter][1]
                            result = math.cos(float(self.__tokens[iter][1]))
                        else:
                            operation += 'Cos('
                            operation += self.__tokens[iter][1]
                            result = math.cos(float(self.__tokens[iter][1]))
                    iter+=1
                operation += ')='
                data.append(['COSENO',operation,result])
            elif line[1] == 'Operacion' and self.__tokens[iterator+2][1]=='TANGENTE':
                iter=iterator
                operation = ''
                result = 0
                while not (self.__tokens[iter][1] == '</' and self.__tokens[iter+1][1] == 'Operacion'):
                    if self.__tokens[iter][0]=='Numero':
                        if operation == '':
                            operation += 'Tan('
                            operation += self.__tokens[iter][1]
                            result = math.tan(float(self.__tokens[iter][1]))
                        else:
                            operation += 'Tan('
                            operation += self.__tokens[iter][1]
                            result = math.tan(float(self.__tokens[iter][1]))
                    iter+=1
                operation += ')='
                data.append(['TANGENTE',operation,result])  
            elif line[1] == 'Operacion' and self.__tokens[iterator+2][1]=='MOD':
                iter=iterator
                operation = ''
                result = 0
                while not (self.__tokens[iter][1] == '</' and self.__tokens[iter+1][1] == 'Operacion'):
                    if self.__tokens[iter][0]=='Numero':
                        if operation == '':
                            operation += self.__tokens[iter][1]
                            result = float(self.__tokens[iter][1])
                        else:
                            operation += 'MOD'
                            operation += self.__tokens[iter][1]
                            result %= float(self.__tokens[iter][1])
                    iter+=1
                operation += '='
                data.append(['MOD',operation,result])
            elif line[1] == 'Titulo' and self.__tokens[iterator+1][1]=='Color' and self.__tokens[iterator+4][1]=='Tamanio':
                if self.__tokens[iterator+3][1]=='ROJO':
                    data.append(['Titulo','Red',self.__tokens[iterator+6][1]])
                elif self.__tokens[iterator+3][1]=='VERDE':
                    data.append(['Titulo','Green',self.__tokens[iterator+6][1]])
                elif self.__tokens[iterator+3][1]=='AZUL':
                    data.append(['Titulo','Blue',self.__tokens[iterator+6][1]])
                elif self.__tokens[iterator+3][1]=='AMARILLO':
                    data.append(['Titulo','Yellow',self.__tokens[iterator+6][1]])
                elif self.__tokens[iterator+3][1]=='ANARANJADO':
                    data.append(['Titulo','Orange',self.__tokens[iterator+6][1]])
            elif line[1] == 'Descripcion' and self.__tokens[iterator+1][1]=='Color' and self.__tokens[iterator+4][1]=='Tamanio':
                if self.__tokens[iterator+3][1]=='ROJO':
                    data.append(['Descripcion','Red',self.__tokens[iterator+6][1]])
                elif self.__tokens[iterator+3][1]=='VERDE':
                    data.append(['Descripcion','Green',self.__tokens[iterator+6][1]])
                elif self.__tokens[iterator+3][1]=='AZUL':
                    data.append(['Descripcion','Blue',self.__tokens[iterator+6][1]])
                elif self.__tokens[iterator+3][1]=='AMARILLO':
                    data.append(['Descripcion','Yellow',self.__tokens[iterator+6][1]])
                elif self.__tokens[iterator+3][1]=='ANARANJADO':
                    data.append(['Descripcion','Orange',self.__tokens[iterator+6][1]])
            elif line[1] == 'Contenido' and self.__tokens[iterator+1][1]=='Color' and self.__tokens[iterator+4][1]=='Tamanio':
                if self.__tokens[iterator+3][1]=='ROJO':
                    data.append(['Contenido','Red',self.__tokens[iterator+6][1]])
                elif self.__tokens[iterator+3][1]=='VERDE':
                    data.append(['Contenido','Green',self.__tokens[iterator+6][1]])
                elif self.__tokens[iterator+3][1]=='AZUL':
                    data.append(['Contenido','Blue',self.__tokens[iterator+6][1]])
                elif self.__tokens[iterator+3][1]=='AMARILLO':
                    data.append(['Contenido','Yellow',self.__tokens[iterator+6][1]])
                elif self.__tokens[iterator+3][1]=='ANARANJADO':
                    data.append(['Contenido','Orange',self.__tokens[iterator+6][1]])

            iterator +=1
        return data