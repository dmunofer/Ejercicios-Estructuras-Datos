class Vista():

    def __init__(self):

        self.entrada=str(input('Primera entrada:'))
        self.entrada2=str(input('Segunda entrada:'))


class Controlador():

    def __init__(self, entrada, entrada2):

        self.primera=str(entrada).upper()
        self.segunda=str(entrada2).upper()
