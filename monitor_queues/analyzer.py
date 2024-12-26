def analyze_queues(file_path, threshold=200):
    """Lee un archivo de colas y notifica si algún valor excede el umbral."""
    try:
        with open(file_path, "r") as file:
            for line in file:
                if "=" in line:
                    queue_name, value = line.strip().split("=")
                    value = int(value)

                    if value > threshold:
                        print(f"⚠️ Notificación: QUEUE Procesamiento Interno XML '{queue_name}' Transacciones encoladas: {value}")
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no fue encontrado.")
    except Exception as e:
        print(f"Error al analizar el archivo: {e}")
