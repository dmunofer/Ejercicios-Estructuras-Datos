class Vista():

    def __init__(self):

        self.entrada=str(input('Primera entrada:'))
        self.entrada2=str(input('Segunda entrada:'))
        controlador = Controlador(self.entrada, self.entrada2)
        Modelo(controlador.primera, controlador.segunda)


class Controlador():

    def __init__(self, entrada, entrada2):

        self.primera=str(entrada).upper()
        self.segunda=str(entrada2).upper()


class Modelo():

    def __init__(self, primera, segunda):
        self.escribe(primera,segunda)

    def escribe(self, filename, primera, segunda):
        file= open(filename, 'w')
        file.write(primera+'\n'+ segunda)
        file.close()
