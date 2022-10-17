
class Deportista:
    def __init__(self, deporte, anios):
        self._deporte = deporte
        self._añosPracticando = anios
        
    def getDeporte(self):
        return self._deporte
    def getAñosPracticando(self):
        return self._añosPracticando

    def setDeporte(self,i):
        self._deporte = i
    def setAñosPracticando(self,i):
        self._añosPracticando
