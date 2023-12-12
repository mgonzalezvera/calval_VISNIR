import mat73
import os


MAIN_FOLDER = '/home/usuario/Documentos/MISION/CalVal/VisNir/'


def process_dark_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        # Imprime la carpeta actual en la estructura
        relative_path = os.path.relpath(root, folder_path)
        print(f"{relative_path}")

        for file in files:
            if file.endswith(".mat"):
                file_path = os.path.join(root, file)

                # Carga el archivo .mat y obtiene el valor (ajusta según tu estructura de datos)
                try:
                    mat_data = mat73.loadmat(file_path)
                    value = mat_data['salida']['tiemposInt']
                    print(f"   - {file}: {value} ms")
                except Exception as e:
                    print(f"   - {file}: No se pudo procesar el archivo ({e})")


# Ruta principal del directorio
path = '20231127_VisNir_INVAP/EOM/Spectral/'
main_folder = MAIN_FOLDER+path

# Procesa cada banda

for band_folder in sorted(os.listdir(main_folder)):
    print('-----------------------------------------------------------------------------------------------------------')
    band_path = os.path.join(main_folder, band_folder)
    # Imprime la banda en la estructura
    print(f"{band_folder}")

    # Verifica si hay una subcarpeta "dark" y procesa solo esa carpeta
    dark_folder = os.path.join(band_path, "dark")
    if os.path.exists(dark_folder):
        process_dark_folder(dark_folder)
    else:
        print("   - No se encontró la carpeta 'dark' en esta banda.")
