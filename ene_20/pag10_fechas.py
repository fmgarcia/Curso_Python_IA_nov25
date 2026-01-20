'''
●Pídele al usuario su fecha de nacimiento en formato dd/mm/yyyy
●Calcula cuantos años y días han pasado desde dicha fecha hasta hoy y
muéstraselo
'''

# Esta versión no tiene en cuenta los años bisiestos
from datetime import datetime
fecha_nacimiento_str = input("Introduce tu fecha de nacimiento (dd/mm/yyyy): ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
diferencia = datetime.now() - fecha_nacimiento
años = diferencia.days // 365 # Años completos
días = diferencia.days % 365 # Días restantes
print(f"Han pasado {años} años y {días} días desde tu nacimiento.")

from dateutil.relativedelta import relativedelta
años = relativedelta(datetime.now(), fecha_nacimiento).years
meses = relativedelta(datetime.now(), fecha_nacimiento).months
días = relativedelta(datetime.now(), fecha_nacimiento).days
print(f"Han pasado {años} años, {meses} meses y {días} días desde tu nacimiento.")