
from deportista import Deportista
from persona import Persona

class Futbolista(Persona, Deportista):
    _listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo,anios,goles,tarjetas,habil):
        Persona().__init__(nombre, edad, altura, sexo)
        Deportista().__init__('Futbol',anios)
        _golesMarcados = goles
        _tarjetasRojas = tarjetas
        _piernaHabil = habil
        Futbolista._listaFutbolistas.append(self)
    
    def getGolesMarcados(self):
        return self._golesMarcados
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def getPiernaHabil(self):
        return self._piernaHabil
    @classmethod
    def getListaFutolistas(cls):
        return cls._listaFutbolistas

    def setGolesMarcados(self,i):
        self._golesMarcados = i
    def setTarjetasRojas(self,i):
        self._tarjetasRojas = i
    def setPiernaHabil(self,i):
        self._piernaHabil = i

    def __str__(self):
        return f'Mi nombre es {self.getNombre} soy profesional en el deporte {self.getDeporte} Tengo {self.getEdad} años de edad y llevo {self.getAñosPracticando} años en el deporte'

