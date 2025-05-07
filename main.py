from estudiantes.registro import cargar_estudiantes, imprimir_tabla, calcular_promedio

def main():
    path= "estudiantes.csv"
    lista=cargar_estudiantes(path)
    imprimir_tabla(lista)
    promedio=calcular_promedio(lista)
    print(f"Promedio general: {promedio:.2f}")
    
if __name__ == "__main__":
    main()