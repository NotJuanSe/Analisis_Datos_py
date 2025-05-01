def analizar_generos(df):
    """
    Realiza análisis relacionados con género
    """
    # Reemplazar espacios en blanco con "Sin Especificar"
    df['Genero'] = df['Genero'].fillna('Sin Especificar')
    df['Genero'] = df['Genero'].replace('', 'Sin Especificar')
    
    # Cantidad por género
    cantidad_genero = df['Genero'].value_counts()
    
    # Porcentaje por género
    porcentaje_genero = (df['Genero'].value_counts() / len(df) * 100).round(2)
    
    return cantidad_genero, porcentaje_genero