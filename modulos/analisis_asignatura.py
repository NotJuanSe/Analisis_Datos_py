import pandas as pd

def analizar_asignaturas(df):
    """
    Realiza análisis relacionados con asignaturas
    """
    # Reemplazar espacios en blanco con "Sin Especificar"
    df['Asginatura'] = df['Asginatura'].fillna('Sin Especificar')
    df['Asginatura'] = df['Asginatura'].replace('', 'Sin Especificar')
    
    # Cantidad de estudiantes por asignatura
    estudiantes_asignatura = df['Asginatura'].value_counts()
    
    # Agrupamiento por género y asignatura
    grupo_gen_asig = pd.crosstab(df['Genero'], df['Asginatura'])
    
    return estudiantes_asignatura, grupo_gen_asig