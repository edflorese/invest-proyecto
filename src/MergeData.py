import os
import pandas as pd

def combine_csv_files(folder_path, output_filename="combined.csv"):
    """
    Combina todos los archivos CSV en una carpeta y guarda el archivo resultante.

    Args:
        folder_path (str): Ruta a la carpeta que contiene los archivos CSV.
        output_filename (str): Nombre del archivo combinado que se guardará. Por defecto, "combined.csv".
    """
    try:
        # Obtener la lista de archivos CSV en la carpeta
        csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

        if not csv_files:
            print("No se encontraron archivos CSV en la carpeta.")
            return

        # Leer y combinar los archivos CSV
        combined_df = pd.DataFrame()
        for file in csv_files:
            file_path = os.path.join(folder_path, file)
            df = pd.read_csv(file_path)
            combined_df = pd.concat([combined_df, df], ignore_index=True)

        # Guardar el archivo combinado
        output_path = os.path.join(folder_path, output_filename)
        combined_df.to_csv(output_path, index=False)
        print(f"Archivo combinado guardado como: {output_path}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Uso del script
if __name__ == "__main__":
    folder_path = input("Introduce la ruta a la carpeta con los archivos CSV: ").strip()
    output_filename = input("Introduce el nombre del archivo combinado (por defecto: combined.csv): ").strip()
    if not output_filename:
        output_filename = "combined.csv"
    combine_csv_files(folder_path, output_filename)
