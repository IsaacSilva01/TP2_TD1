from haversine import haversine, Unit

class CampanaVerde:
    def _init_(self, direccion:str, barrio:str, comuna:int, materiales:set[str], latitud:float, longitud:float):
        '''Inicializa una CampanaVerde con nombre, direccion, barrio, comuna, materiales, latitud y longitud.'''
        #Creamos los atributos del objeto CampanaVerde
        self.direccion:str = direccion
        self.barrio:str = barrio
        self.comuna:int = comuna
        self.materiales:set[str] = materiales
        self.latitud:float = latitud
        self.longitud:float = longitud

    def distancia(self, lat:float, lng:float)-> float:
        '''
        Requiere: Nada
        Devuelve: La distancia entre la CampanaVerde y el punto ingresado
        (punto dado por la latitud y la longitud con las cuales el método fue invocado)
        '''
        #Utilizamos la función importada haversine para calcular la distancia
        return haversine((self.latitud, self.longitud), (lat, lng), unit = Unit.METERS)

    def _repr_(self) -> str:
        ''' Devuelve una representación string de la CampanaVerde. '''
        return "<" + self.direccion + "@" + "/".join(list(self.materiales)) + "@" + self.barrio + ">"