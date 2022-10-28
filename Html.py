import math

class Html:
    def __init__(self, path='', errors=[], tokens=[]) -> None:
        self.__path = path.split('/')[-1]
        self.__path = self.__path[:self.__path.find('.')]
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
        text = f'<html><head><title>LFPA+ - Proyecto 2</title><link href="{self.__path}.css" rel="stylesheet" type="text/css"/></head><body>'
        for component in self.__components:
            if component[13] == 'this':
                if component[4] is None:
                        component[4] = ''
                if component[6] is None:
                        component[6] = 'left'
                if component[8] is None:
                        component[8] = ''
                if component[14] == 'Etiqueta':
                    text += f'<label id="{component[2]}">{component[4]}'
                    if len(component[12]) != 0:
                        text = self.__addComponentToHtml(component[12],text)
                    text += '</label>'
                elif component[14] == 'Boton':
                    text += f'<input type="submit" id="{component[2]}" value="{component[4]}" style="text-align: {component[6]}"/>'
                elif component[14] == 'Check':
                    if component[7] == 'True':
                        text += f'<input type="checkbox" id="{component[2]}" checked/>'
                    else:
                        text += f'<input type="checkbox" id="{component[2]}"/>'
                elif component[14] == 'RadioBoton':
                    if component[7] == 'True':
                        text += f'<input type="radio" name="{component[8]}" id="{component[2]}" checked/>'
                    else:
                        text += f'<input type="radio" name="{component[8]}" id="{component[2]}"/>'
                elif component[14] == 'Texto':
                    text += f'<input type="text" id="{component[2]}" value="{component[4]}" style="text-align: {component[6]}"/>'
                elif component[14] == 'AreaTexto':
                    text += f'<TEXTAREA id="{component[2]}">{component[4]}</TEXTAREA>'
                elif component[14] == 'Clave':
                    text += f'<input type="password" id="{component[2]}" value="{component[4]}" style="text-align: {component[6]}"/>'
                elif component[14] == 'Contenedor':
                    text += f'<div id="{component[2]}">'
                    if len(component[12]) != 0:
                        text = self.__addComponentToHtml(component[12],text)
                    text += '</div>'
        text += '</body></html>'
        file=open(f'Resultados/{self.__path}.html','w',encoding='utf-8')
        file.write(text)
        file.close()

    def __generateCSS(self):
        text = ''
        for component in self.__components:
            if component[11] is None:
                component[11] = ['0','0']
            if component[9] is None:
                component[9] = '100'
            if component[10] is None:
                component[10] = '25'
            if component[14] == 'Etiqueta':
                if component[3] is None and component[5] is not None:
                    text += f'#{component[2]}'+'{'+ f'position:absolute; top: {component[11][1]}px; left: {component[11][0]}px; width: {component[9]}; height: {component[10]}; background-color: rgb({component[5][0]},{component[5][1]},{component[5][2]}); font-size: 12px;'+'}'
                elif component[3] is not None and component[5] is None:
                    text += f'#{component[2]}'+'{'+ f'position:absolute; top: {component[11][1]}px; left: {component[11][0]}px; width: {component[9]}; height: {component[10]}; color: rgb({component[3][0]},{component[3][1]},{component[3][2]}); font-size: 12px;'+'}'
                elif component[3] is not None and component[5] is not None:
                    text += f'#{component[2]}'+'{'+ f'position:absolute; top: {component[11][1]}px; left: {component[11][0]}px; width: {component[9]}; height: {component[10]}; color: rgb({component[3][0]},{component[3][1]},{component[3][2]}); background-color: rgb({component[5][0]},{component[5][1]},{component[5][2]}); font-size: 12px;'+'}'
                else:
                    text += f'#{component[2]}'+'{'+ f'position:absolute; top: {component[11][1]}px; left: {component[11][0]}px; width: {component[9]}; height: {component[10]}; font-size: 12px;'+'}'
            elif component[14] == 'Boton':
                text += f'#{component[2]}'+'{'+ f'position:absolute; top: {component[11][1]}px; left: {component[11][0]}px; width: 100; height: 25; font-size: 12px;'+'}'
            elif component[14] == 'Check':
                text += f'#{component[2]}'+'{'+ f'position:absolute; top: {component[11][1]}px; left: {component[11][0]}px; width: 100; height: 25; font-size: 12px;'+'}'
            elif component[14] == 'RadioBoton':
                text += f'#{component[2]}'+'{'+ f'position:absolute; top: {component[11][1]}px; left: {component[11][0]}px; width: 100; height: 25; font-size: 12px;'+'}'
            elif component[14] == 'Texto':
                text += f'#{component[2]}'+'{'+ f'position:absolute; top: {component[11][1]}px; left: {component[11][0]}px; width: 100; height: 25; font-size: 12px;'+'}'
            elif component[14] == 'AreaTexto':
                text += f'#{component[2]}'+'{'+ f'position:absolute; top: {component[11][1]}px; left: {component[11][0]}px; width: 150; height: 150; font-size: 12px;'+'}'
            elif component[14] == 'Clave':
                text += f'#{component[2]}'+'{'+ f'position:absolute; top: {component[11][1]}px; left: {component[11][0]}px; width: 100; height: 25; font-size: 12px;'+'}'
            elif component[14] == 'Contenedor':
                if component[5] is not None:
                    text += f'#{component[2]}'+'{'+ f'position:absolute; top: {component[11][1]}px; left: {component[11][0]}px; width: {component[9]}; height: {component[10]}; background-color: rgb({component[5][0]},{component[5][1]},{component[5][2]}); font-size: 12px;'+'}'
                else:
                    text += f'#{component[2]}'+'{'+ f'position:absolute; top: {component[11][1]}px; left: {component[11][0]}px; width: {component[9]}; height: {component[10]}; font-size: 12px;'+'}'
        file=open(f'Resultados/{self.__path}.css','w',encoding='utf-8')
        file.write(text)
        file.close()

    def __generateComponents(self):
        self.__components = []

        i=0
        for token in self.__tokens:
            try:
                if token[2] == 12 and self.__tokens[i+1][2] == 2 and self.__tokens[i+2][2] == 3:
                    self.__components.append([token[2],token[1],self.__tokens[i+1][3],None,None,None,None,None,None,None,None,None,[],None,token[3]])
                elif token[2] == 2 and self.__tokens[i+1][2] == 5 and self.__tokens[i+2][2] == 2 and self.__tokens[i+3][2] == 6:
                    if self.__tokens[i+2][3] == 'setColorLetra':
                        component = self.__searchComponentById(token[3])
                        if component is not None:
                            j=i+4
                            numlist = []
                            while self.__tokens[j][2] == 8:
                                numlist.append(self.__tokens[j][3])
                                j+=2  
                            component[3] = numlist
                            self.__setComponentById(component[2],component)
                    elif self.__tokens[i+2][3] == 'setTexto':
                        component = self.__searchComponentById(token[3])
                        if component is not None:
                            if self.__tokens[i+4][2] == 9 and self.__tokens[i+5][2] == 2:
                                component[4] = self.__tokens[i+5][3]
                                self.__setComponentById(component[2],component)
                    elif self.__tokens[i+2][3] == 'setAlineacion':
                        component = self.__searchComponentById(token[3])
                        if component is not None:
                            if self.__tokens[i+4][3] in ['Centro','Izquierdo','Derecho']:
                                if self.__tokens[i+4][3] == 'Centro':
                                    component[6] = 'center'
                                elif self.__tokens[i+4][3] == 'Izquierdo':
                                    component[6] = 'left'
                                elif self.__tokens[i+4][3] == 'Derecho':
                                    component[6] = 'right'
                            else:
                                component[6] = 'left'
                            self.__setComponentById(component[2],component)
                    elif self.__tokens[i+2][3] == 'setColorFondo':
                        component = self.__searchComponentById(token[3])
                        if component is not None:
                            j=i+4
                            numlist = []
                            while self.__tokens[j][2] == 8:
                                numlist.append(self.__tokens[j][3])
                                j+=2  
                            component[5] = numlist
                            self.__setComponentById(component[2],component)
                    elif self.__tokens[i+2][3] == 'setMarcada':
                        component = self.__searchComponentById(token[3])
                        if component is not None:
                            if self.__tokens[i+4][3] == 'True':
                                component[7] = self.__tokens[i+4][3]
                            else:
                                component[7] = 'False'
                            self.__setComponentById(component[2],component)
                    elif self.__tokens[i+2][3] == 'setGrupo':
                        component = self.__searchComponentById(token[3])
                        if component is not None:
                            if self.__tokens[i+4][2] == 2:
                                id = self.__searchComponentById(self.__tokens[i+4][3])
                                if id is not None:
                                    component[8] = self.__tokens[i+4][3]
                            self.__setComponentById(component[2],component)
                    elif self.__tokens[i+2][3] == 'setAncho':
                        component = self.__searchComponentById(token[3])
                        if component is not None:
                            if self.__tokens[i+4][2] == 8:
                                component[9] = self.__tokens[i+4][3]
                            self.__setComponentById(component[2],component)
                    elif self.__tokens[i+2][3] == 'setAlto':
                        component = self.__searchComponentById(token[3])
                        if component is not None:
                            if self.__tokens[i+4][2] == 8:
                                component[10] = self.__tokens[i+4][3]
                            self.__setComponentById(component[2],component)
                    elif self.__tokens[i+2][3] == 'setPosicion':
                        component = self.__searchComponentById(token[3])
                        if component is not None:
                            j=i+4
                            numlist = []
                            while self.__tokens[j][2] == 8:
                                numlist.append(self.__tokens[j][3])
                                j+=2  
                            component[11] = numlist
                            self.__setComponentById(component[2],component)
                    elif self.__tokens[i+2][3] == 'add':
                        if token[3] != 'this':
                            component = self.__searchComponentById(token[3])
                            if component is not None:
                                id = self.__searchComponentById(self.__tokens[i+4][3])
                                if id is not None:
                                    component[12].append(self.__tokens[i+4][3])
                                    self.__setComponentById(component[2],component)
                        else:
                            component = self.__searchComponentById(self.__tokens[i+4][3])
                            if component is not None:
                                component[13] = token[3]
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

    def __addComponentToHtml(self,components, text):
        for compo in components:
            component = self.__searchComponentById(compo)
            if component[4] is None:
                component[4] = ''
            if component[6] is None:
                component[6] = 'left'
            if component[8] is None:
                component[8] = ''
            if component[14] == 'Etiqueta':
                text += f'<label id="{component[2]}">{component[4]}'
                if len(component[12]) != 0:
                    text = self.__addComponentToHtml(component[12],text)
                text += '</label>'
            elif component[14] == 'Boton':
                text += f'<input type="submit" id="{component[2]}" value="{component[4]}" style="text-align: {component[6]}"/>'
            elif component[14] == 'Check':
                if component[7] == 'True':
                    text += f'<input type="checkbox" id="{component[2]}" checked/>'
                else:
                    text += f'<input type="checkbox" id="{component[2]}"/>'
            elif component[14] == 'RadioBoton':
                if component[7] == 'True':
                    text += f'<input type="radio" name="{component[8]}" id="{component[2]}" checked/>'
                else:
                    text += f'<input type="radio" name="{component[8]}" id="{component[2]}"/>'
            elif component[14] == 'Texto':
                text += f'<input type="text" id="{component[2]}" value="{component[4]}" style="text-align: {component[6]}"/>'
            elif component[14] == 'AreaTexto':
                text += f'<TEXTAREA id="{component[2]}">{component[4]}</TEXTAREA>'
            elif component[14] == 'Clave':
                text += f'<input type="password" id="{component[2]}" value="{component[4]}" style="text-align: {component[6]}"/>'
            elif component[14] == 'Contenedor':
                text += f'<div id="{component[2]}">'
                if len(component[12]) != 0:
                    text = self.__addComponentToHtml(component[12],text)
                text += '</div>'
        return text