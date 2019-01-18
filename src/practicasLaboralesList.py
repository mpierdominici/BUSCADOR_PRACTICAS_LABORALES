from practicaLaboral import practicaLaboral
import csv
#practicasLaboralesList
#crea la lista de practocas laborales, a partir del path de la base de datos
#
#
class practicasLaboralesList:
    def __init__(self, path : str):
        self.path = path
        self.listaPracticasLaborales = []
        with open(self.path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.listaPracticasLaborales.append(practicaLaboral(row[0],row[1],row[2],row[3],row[4],row[5].split('-'),row[6]))


