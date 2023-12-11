import os
from mat73 import loadmat
path = '/home/maxpower/Documentos/SABIA_MAR/VISNIR/VISNIR/DATOS_CRUDOS/20231127_VisNir_INVAP'


def buscar_archivos_mat_recursivo(ruta_directorio):
    archivos_mat = []
    for directorio_actual, _, archivos in os.walk(ruta_directorio):
        for archivo in archivos:
            if archivo.endswith(".mat"):
                archivos_mat.append(os.path.join(directorio_actual, archivo))
    return archivos_mat


def cargar_y_mostrar_resultados_recursivo(ruta_directorio):
    archivos_mat = buscar_archivos_mat_recursivo(ruta_directorio)
    exitos = 0
    fallos = 0
    archivos_fallidos = []

    # Imprimir encabezado de la tabla
    print("| Nombre del Archivo | Resultado |")
    print("|---------------------|-----------|")

    for archivo in archivos_mat:
        try:
            # Intentar cargar el archivo .mat
            loadmat(archivo)
            resultado = "Éxito"
            exitos += 1
        except Exception as e:
            resultado = f"Fallo ({str(e)})"
            fallos += 1
            archivos_fallidos.append(archivo)

        # Imprimir fila de la tabla
        print(f"| {archivo} | {resultado} |")

    # Imprimir resumen de éxitos y fallos
    print("\nResumen:")
    print(f"Éxitos: {exitos}")
    print(f"Fallos: {fallos}")

    # Imprimir archivos que fallaron
    if archivos_fallidos:
        print("\nArchivos que fallaron:")
        for archivo_fallido in archivos_fallidos:
            print(archivo_fallido)


if __name__ == "__main__":
    # Ruta del directorio principal donde se inicia la búsqueda
    ruta_directorio = path

    cargar_y_mostrar_resultados_recursivo(ruta_directorio)