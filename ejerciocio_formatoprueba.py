import csv 
from datetime import datetime 
bitacora=[]
def agregar_evento(evento):
    fecha_hora_actual= datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    fecha_evento= f"{fecha_hora_actual} - {evento}"
    bitacora.append(fecha_evento)
    print(f"evento '{evento}' registrado en la bitacora del auto.")
