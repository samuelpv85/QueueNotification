from monitor_queues.notifier import send_windows_notification, send_telegram_notification

# Diccionario con los mensajes personalizados para cada cola
queue_descriptions = {
    "GEOINTEGRATION.IN.XML.TRANSACTION.QUEUE": "Transacciones encoladas XML Procesamiento interno del Integrador",
    "GEOINTEGRATION.SAVE.FOID.SALE.QUEUE": "Transacciones encoladas hacia el SQL SERVER",
    "GEOINTEGRATION.SAVE.FOID.HECHAUKA.QUEUE": "Transacciones encoladas hacia el SQL SERVER - RESUMEN HECHAUKA",
    "GEOINTEGRATION.SAVE.RRHH.QUEUE": "Transacciones encoladas hacia la BBDD SICS",
    "GEOINTEGRATION.SAVE.FOID.GAMBLING.QUEUE": "Transacciones encoladas hacia la BBDD SICS",
    "GEOINTEGRATION.SAVE.FOID.CONCILIATOR.QUEUE": "Transacciones encoladas hacia la BBDD ORACLE GEOCONCILIADOR2",
    "GEOINTEGRATION.SAVE.TRANSACTION.MONGO.QUEUE": "Transacciones encoladas hacia la BBDD MONGO",
    "GEOINTEGRATION.SAVE.FOID.SERVICES.QUEUE": "Transacciones encoladas hacia SQL SERVER - SERVICIOS",
    "GEOINTEGRATION.FOID.HANA.SERVICES.QUEUE": "Transacciones encoladas hacia la SAPCAR",
    "ERROR.QUEUE": "Transacciones en ERROR"
}

def analyze_queues(file_path, threshold=200):
    """Lee un archivo de colas y notifica si algún valor excede el umbral con mensaje personalizado."""
    try:
        with open(file_path, "r") as file:
            for line in file:
                if "=" in line:
                    queue_name, value = line.strip().split("=")
                    value = int(value)

                    # Verificar si el valor excede el umbral
                    if value > threshold:
                        # Obtener la descripción de la cola, si existe
                        description = queue_descriptions.get(queue_name, "Descripción no disponible")

                        # Crear el mensaje personalizado
                        message = f"⚠️ Notificación: QUEUE -> {queue_name} -> {description}: {value}."

                        # Imprimir el mensaje en consola (lo que ya haces)
                        print(message)

                        # Enviar notificación a Windows
                        send_windows_notification(queue_name, value, description)

                        # Enviar notificación a Telegram
                        send_telegram_notification(queue_name, value, description)

    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no fue encontrado.")
    except Exception as e:
        print(f"Error al analizar el archivo: {e}")
