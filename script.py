import httpx
import json
import csv
import argparse
from typing import List, Dict

# Constantes predeterminadas
DEFAULT_URL = "https://storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/product.json"
DEFAULT_OUTPUT_CSV_FILE = "output.csv"

# Definir las claves que estamos buscando
CLAVES_BUSCADAS = [
    "allergens", "sku", "vegan", "kosher", "organic", "vegetarian", 
    "gluten_free", "lactose_free", "package_quantity", "unit_size", "net_weight"
]

# Estructura para almacenar los resultados
RESULTADO_DEFAULT = {
    "allergens": None,
    "sku": None,
    "vegan": None,
    "kosher": None,
    "organic": None,
    "vegetarian": None,
    "gluten_free": None,
    "lactose_free": None,
    "package_quantity": None,
    "unit_size": None,
    "net_weight": None,
}


def obtener_datos_json(url: str) -> List[Dict]:
    """Obtiene los datos JSON desde una URL y extrae el atributo 'attributesRaw'."""
    try:
        response = httpx.get(url)
        response.raise_for_status()  # Lanza un error si la respuesta no es exitosa (código 4xx o 5xx)
        data = response.json()
        return data["allVariants"][0]["attributesRaw"]
    except httpx.RequestError as e:
        print(f"Error de solicitud HTTP: {e}")
        return []
    except (KeyError, ValueError) as e:
        print(f"Error procesando la respuesta JSON: {e}")
        return []


def procesar_custom_attributes(data: List[Dict]) -> Dict:
    """Procesa los 'custom_attributes' y extrae las claves buscadas."""
    resultado = RESULTADO_DEFAULT.copy()

    for dic in data:
        if dic["name"] == "custom_attributes":
            # Convertir el valor "es-CR" a un diccionario de Python
            try:
                custom_attributes = json.loads(dic["value"]["es-CR"])
                for k, v in custom_attributes.items():
                    if k in CLAVES_BUSCADAS:
                        if k == "allergens":
                            resultado[k] = [v["value"][0]["code"]]
                        else:
                            resultado[k] = v["value"]
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error procesando los atributos personalizados: {e}")

    return resultado


def guardar_como_csv(data: List[Dict], file_name: str):
    """Guarda la lista de diccionarios como un archivo CSV."""
    try:
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = data[0].keys()  # Las claves del primer diccionario como encabezados
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"CSV guardado como {file_name}")
    except Exception as e:
        print(f"Error guardando el archivo CSV: {e}")


def main(url: str, output_file: str):
    """Función principal que orquesta el flujo de obtención de datos, procesamiento y exportación a CSV."""
    # Obtener los datos JSON
    data = obtener_datos_json(url)
    
    if data:
        # Procesar los datos de "custom_attributes"
        resultado = procesar_custom_attributes(data)
        
        # Guardar el resultado como un archivo CSV
        guardar_como_csv([resultado], output_file)
    else:
        print("No se pudieron obtener datos válidos.")


if __name__ == "__main__":
    # Configurar argparse para permitir la entrada de parámetros desde la terminal
    parser = argparse.ArgumentParser(description="Script para descargar un JSON, procesarlo y guardar en un archivo CSV.")
    parser.add_argument(
        "--url", 
        type=str, 
        default=DEFAULT_URL, 
        help="URL del archivo JSON (predeterminado: %(default)s)"
    )
    parser.add_argument(
        "--output", 
        type=str, 
        default=DEFAULT_OUTPUT_CSV_FILE, 
        help="Nombre del archivo CSV de salida (predeterminado: %(default)s)"
    )
    
    # Parsear los argumentos de la línea de comandos
    args = parser.parse_args()
    
    # Ejecutar el flujo principal con los parámetros proporcionados
    main(args.url, args.output)
