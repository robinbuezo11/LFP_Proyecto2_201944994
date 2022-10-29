class PDA:
    def __init__(self,errors=[],tokens=[]) -> None:
        self.__errornum = len(errors)+1
        self.__tokennum = len(tokens)+1
        self.__errors = errors
        self.__tokens = tokens

    def analyze(self):

        stack = ['#','S0']

        i = 1
        for token in self.__tokens:
            while stack[-1] not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14]:
                if stack[-1] == 'S0':
                    stack.pop()
                    stack.append('S3')
                    stack.append('S2')
                    stack.append('S1')
                elif stack[-1] == 'S1':
                    stack.pop()
                    stack.append(4)
                    stack.append(11)
                    stack.append('S4')
                    stack.append(11)
                    stack.append(1)
                elif stack[-1] == 'S2':
                    stack.pop()
                    stack.append(4)
                    stack.append(13)
                    stack.append('S5')
                    stack.append(13)
                    stack.append(1)
                elif stack[-1] == 'S3':
                    stack.pop()
                    stack.append(4)
                    stack.append(14)
                    stack.append('S5')
                    stack.append(14)
                    stack.append(1)
                elif stack[-1] == 'S4':
                    if token[2] == 12:
                        stack.pop()
                        stack.append('S4')
                        stack.append(3)
                        stack.append(2)
                        stack.append(12)
                    else:
                        stack.pop()
                elif stack[-1] == 'S5':
                    if token[2] == 2:
                        stack.pop()
                        stack.append('S5')
                        stack.append(3)
                        stack.append(7)
                        stack.append('S6')
                        stack.append(6)
                        stack.append(2)
                        stack.append(5)
                        stack.append(2)
                    else:
                        stack.pop()
                elif stack[-1] == 'S6':
                    if token[2] == 8:
                        stack.pop()
                        stack.append('S7')
                        stack.append(8)
                    elif token[2] == 9:
                        stack.pop()
                        stack.append(9)
                        stack.append('S8')
                        stack.append(9)
                    elif token[2] == 2:
                        stack.pop()    
                        stack.append(2)
                    else:
                        self.__errors.append([self.__errornum,'Sintático',token[4],token[5],token[3],f'Error cerca de {token[3]}'])
                        return
                elif stack[-1] == 'S7':
                    if token[2] == 10:
                        stack.pop()
                        stack.append('S7')
                        stack.append(8)
                        stack.append(10)
                    else:
                        stack.pop()
                elif stack[-1] == 'S8':
                    if token[2] == 2:
                        stack.pop()
                        stack.append('S8')
                        stack.append(2)
                    elif token[2] == 8:
                        stack.pop()
                        stack.append('S8')
                        stack.append(8)
                    else:
                        stack.pop()
                else:
                    self.__errors.append([self.__errornum,'Sintático',token[4],token[5],token[3],f'Error cerca de {token[3]}'])
                    return
            if token[2] in [1,2,3,4,5,6,7,8,9,10,11,12,13,14]:
                if stack[-1] == token[2]:
                    stack.pop()
                else:
                    self.__errors.append([self.__errornum,'Sintático',token[4],token[5],token[3],f'Error cerca de {token[3]}'])
                    return
            i+=1

    def getErrors(self):
        return self.__errors

    def getTokens(self):
        return self.__tokens