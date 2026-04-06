import os
from datetime import datetime


ARCHIVO_ENTRADA = input("Ingrese el nombre del archivo de historial (con extensión .txt): ")  
ARCHIVO_SALIDA = "historial_validado.txt"       
ARCHIVO_ERRORES = "errores_historial.log"       



def validar_fecha(fecha_str):
    """
    Valida que la fecha tenga formato YYYY-MM-DD.
    Retorna la fecha si es válida, o None si es incorrecta.
    """
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return fecha_str
    except ValueError:
        return None


def validar_distancia(distancia_str):
    """
    Valida que la distancia sea un número positivo.
    """
    try:
        distancia = float(distancia_str)
        return distancia if distancia > 0 else None
    except ValueError:
        return None


def validar_costo(costo_str):
    """
    Valida que el costo sea un número decimal válido.
    """
    try:
        return float(costo_str)
    except ValueError:
        return None




def procesar_historial():
    """
    Lee el archivo de historial, valida cada línea,
    corrige lo posible y genera archivos de salida.
    """

    
    if not os.path.exists(ARCHIVO_ENTRADA):
        print(f"El archivo {ARCHIVO_ENTRADA} no existe.")
        return


    with open(ARCHIVO_ENTRADA, "r", encoding="utf-8") as entrada, \
         open(ARCHIVO_SALIDA, "w", encoding="utf-8") as salida, \
         open(ARCHIVO_ERRORES, "w", encoding="utf-8") as errores:

        for linea in entrada:
            linea = linea.strip()

            
            if not linea:
                continue

            
            partes = linea.split(";")
            if len(partes) != 3:
                errores.write(f"Formato incorrecto: {linea}\n")
                continue

            fecha, distancia, costo = partes

            
            fecha_valida = validar_fecha(fecha)
            distancia_valida = validar_distancia(distancia)
            costo_valido = validar_costo(costo)

            
            if not fecha_valida or not distancia_valida or costo_valido is None:
                errores.write(f"Error en línea: {linea}\n")
                continue

            
            salida.write(f"{fecha_valida};{distancia_valida};{costo_valido}\n")

    print(f"Archivo de historial procesado: {ARCHIVO_SALIDA}")    

    print("Proceso completado. Revisa historial_validado.txt y errores_historial.log")
    
if __name__ == "__main__":
    procesar_historial()