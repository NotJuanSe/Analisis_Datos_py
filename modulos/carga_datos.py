import pandas as pd

def cargar_datos(ruta_archivo):
    """
    Carga los datos del archivo CSV y muestra información sobre las columnas
    """
    try:
        df = pd.read_csv(ruta_archivo)
        print("\nColumnas disponibles en el CSV:")
        print(df.columns.tolist())
        return df
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None