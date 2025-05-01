import pandas as pd

def analizar_edades(df):
    """
    Realiza análisis por grupos de edad
    """
    df['grupo_edad'] = pd.cut(df['Edad'], 
                             bins=[15, 30, 45, 60], 
                             labels=['16-30', '31-45', '46-60'])
    return df['grupo_edad'].value_counts()