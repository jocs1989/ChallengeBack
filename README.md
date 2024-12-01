# ChallengeBack

¡Bienvenido! Nos gustaría saber más acerca de tus increíbles habilidades como **Back End Developer** y **Scrappers**, y la mejor manera es demostrarnos lo que eres capaz de lograr. Este proyecto consiste en crear un **script en Python** que procesa un archivo JSON, extrae propiedades específicas y las convierte en un archivo CSV.

## Descripción del desafío

El objetivo de este desafío es crear un script que obtenga y dé formato a las siguientes propiedades de un archivo JSON:

- `allergens`
- `sku`
- `vegan`
- `kosher`
- `organic`
- `vegetarian`
- `gluten_free`
- `lactose_free`
- `package_quantity`
- `Unit_size`
- `net_weight`

Estas propiedades se encuentran dentro de un nodo llamado **`custom_attributes`** en el archivo JSON.

### URL del archivo JSON
https://storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/product.json
### Salida esperada en formato CSV

https://storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/output-product.csv


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