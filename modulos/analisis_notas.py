import pandas as pd

def analizar_notas(df):
    """
    Realiza análisis de notas por asignatura
    """
    # Reemplazar espacios en blanco en asignatura con "Sin Especificar"
    df['Asginatura'] = df['Asginatura'].fillna('Sin Especificar')
    df['Asginatura'] = df['Asginatura'].replace('', 'Sin Especificar')
    
    # Nota máxima por asignatura
    nota_max = df.groupby('Asginatura')['Nota'].max()
    
    # Promedio por asignatura (ignorando valores nulos)
    nota_promedio = df.groupby('Asginatura')['Nota'].mean().round(2)
    
    # Análisis de aprobados y reprobados
    df['estado'] = df['Nota'].apply(lambda x: 'Aprobado' if x >= 3.0 else 'Reprobado' if pd.notnull(x) else 'Sin Nota')
    resultado = pd.crosstab(df['Asginatura'], df['estado'])
    
    return nota_max, nota_promedio, resultado