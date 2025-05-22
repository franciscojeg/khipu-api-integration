# Importamos la librería 'requests' para hacer peticiones web
import requests
import json # Librería para trabajar con datos en formato JSON

# --- Tus Credenciales de Khipu (API v3) ---
# Tu API Key real
API_KEY = '869e67ff-8078-475e-a004-34fb2353fbe3'

# --- URL de la API de Khipu para crear cobros (Versión 3) ---
API_URL = 'https://payment-api.khipu.com/v3/payments' # Usamos la URL de la API v3

# --- Datos del Cobro que queremos crear ---
payload = {
    'amount': 5000,
    'currency': 'CLP',
    'subject': 'Cobro de prueba - API v3', # Un título para el cobro
    # Si la API v3 soporta DemoBank con un campo similar a 'bank_id', agrégalo aquí.
    # Por ejemplo: 'bank_id': 'demobank',
    # También, si la API v3 usa 'return_url' y 'cancel_url', podrías añadirlas:
    # 'return_url': 'http://localhost:8000/success_v3',
    # 'cancel_url': 'http://localhost:8000/cancel_v3',
}

# --- Preparar los encabezados (headers) para la petición ---
headers = {
    'Content-Type': 'application/json',
    'x-api-key': API_KEY # Enviamos nuestra API Key aquí
}

# Hacemos la petición POST a la API de Khipu
print("Realizando la petición a Khipu (API v3) para crear el cobro...")
try:
    response = requests.post(
        API_URL,
        json=payload,
        headers=headers
    )

    # Verificamos la respuesta de Khipu
    if response.status_code in [200, 201]:
        print("¡Cobro creado exitosamente con API v3!")
        data = response.json()
        print("Información del cobro:")
        print(json.dumps(data, indent=4))

        payment_url = data.get('payment_url') # O el nombre del campo que use la API v3 para la URL de pago
        if payment_url:
            print(f"\nURL de pago para el cliente: {payment_url}")
            print("Por favor, abre esta URL en tu navegador web para completar el pago.")
        else:
            print("Advertencia: No se encontró una URL de pago directa en la respuesta de la API v3.")
            print("Por favor, consulta la documentación de la API v3 para saber cómo obtener la URL de pago.")

    else:
        print(f"Error al crear el cobro. Código de estado: {response.status_code}")
        print("Mensaje de error de Khipu:")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Ocurrió un error al conectar con la API de Khipu: {e}")