# ChallengeBack

Este proyecto permite obtener un archivo JSON desde una URL, procesarlo y guardar ciertos datos en un archivo CSV. Puedes ejecutar el script directamente desde la terminal y personalizar los parámetros, como la URL del archivo JSON y el nombre del archivo CSV de salida.

## Requisitos

- Python 3.x
- Paquetes necesarios: `httpx`, `json`, `csv`, `argparse`

Para instalar las dependencias, puedes usar `pip`:

```bash
pip install httpx

```

### Usar la URL y el nombre de archivo predeterminado
Para ejecutar el script con la URL y el archivo CSV predeterminados, simplemente corre el siguiente comando en la terminal:
```bash
python process_json_to_csv.py

```
### Proporcionar una URL personalizada

Si deseas proporcionar una URL personalizada para el archivo JSON, puedes hacerlo con el parámetro --url:
```bash
python process_json_to_csv.py --url "https://storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/product.json"

```

### Proporcionar una URL personalizada
Si también deseas especificar un nombre diferente para el archivo CSV de salida, puedes usar el parámetro --output junto con la URL personalizada:

```bash
python process_json_to_csv.py --url "https://nueva_url.com/product.json" --output "resultado.csv"

```