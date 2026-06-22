import json

file_path = "Humedales_Urbanos.geojson"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    features = data.get('features', [])
    if features:
        # Extraemos las propiedades del primer feature
        properties = features[0].get('properties', {})
        print("Atributos y un ejemplo de su valor:")
        print("-" * 50)
        for key, value in properties.items():
            print(f"- **{key}**: {value}")
    else:
        print("No se encontraron features en el archivo.")
except Exception as e:
    print(f"Error al leer el archivo: {e}")
