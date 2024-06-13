import csv
from campana_verde import CampanaVerde

class DataSetCampanasVerdes:
    def _init_(self, archivo_csv:str):
        '''Inicializa un DataSet de las CampanasVerdes obtenidas del archivo_csv'''
        
        self.lista_campanas:list[CampanaVerde]= []
        archivo = open(archivo_csv, encoding = "UTF-8")
        
        for linea in csv.DictReader(archivo):
            direccion:str = linea["direccion"]
            barrio:str = linea["barrio"]
            comuna:int = linea["comuna"]
            materiales:set[str] = set((linea["materiales"]).split("/"))
            coordenadas:str = linea["WKT"]
            campana:CampanaVerde = CampanaVerde(direccion, barrio, comuna, materiales, latitud, longitud)
            self.lista_campanas.append(campana)
            
        archivo.close()
            
    def tamano(self) -> int:
        '''Devuelve la cantidad de campanas verdes del dataset'''
        return len(self.lista_campanas)

    def barrios(...) -> ...:
        ''' completar docstring '''
        pass

    def campanas_del_barrio(...) -> ...:
        ''' completar docstring '''
        pass

    def cantidad_por_barrio(...) -> ...:
        ''' completar docstring '''
        pass

    def tres_campanas_cercanas(...) -> ...:
        ''' completar docstring '''
        pass

    def exportar_por_materiales(...) -> ...:
        ''' completar docstring '''
        pass