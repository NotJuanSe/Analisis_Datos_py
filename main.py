from modulos.carga_datos import cargar_datos
from modulos.analisis_genero import analizar_generos
from modulos.analisis_asignatura import analizar_asignaturas
from modulos.analisis_edad import analizar_edades
from modulos.analisis_notas import analizar_notas

def main():
    # Cargar datos
    ruta_archivo = 'MOCK_DATA.csv'
    df = cargar_datos(ruta_archivo)
    
    if df is None:
        return
    
    # Realizar análisis
    print("\n=== Análisis de Géneros ===")
    cantidad_genero, porcentaje_genero = analizar_generos(df)
    print("Cantidad por género:")
    for genero, cantidad in cantidad_genero.items():
        print(f"- {genero}: {cantidad} estudiantes")
    
    print("\nPorcentaje por género:")
    for genero, porcentaje in porcentaje_genero.items():
        print(f"- {genero}: {porcentaje}%")
    
    print("\n=== Análisis de Asignaturas ===")
    estudiantes_asignatura, grupo_gen_asig = analizar_asignaturas(df)
    print("Estudiantes por asignatura:")
    for asignatura, cantidad in estudiantes_asignatura.items():
        print(f"- {asignatura}: {cantidad} estudiantes")
    
    print("\nAgrupamiento por género y asignatura:")
    print(grupo_gen_asig.to_string())
    
    print("\n=== Análisis por Edades ===")
    grupos_edad = analizar_edades(df)
    for grupo, cantidad in grupos_edad.items():
        print(f"- {grupo}: {cantidad} estudiantes")
    
    print("\n=== Análisis de Notas ===")
    nota_max, nota_promedio, resultado = analizar_notas(df)
    print("Nota máxima por asignatura:")
    for asignatura, nota in nota_max.items():
        print(f"- {asignatura}: {nota:.2f}")
    
    print("\nPromedio por asignatura:")
    for asignatura, promedio in nota_promedio.items():
        print(f"- {asignatura}: {promedio:.2f}")
    
    print("\nAprobados y reprobados por asignatura:")
    print(resultado.to_string())

if __name__ == "__main__":
    main()