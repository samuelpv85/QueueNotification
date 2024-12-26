import requests
from plyer import notification

# Configuración de Telegram
from monitor_queues.config import telegram_config

def send_windows_notification(queue_name, queue_value):
    """Envía una notificación al sistema operativo Windows."""
    try:
        message = f"⚠️ Notificación: QUEUE {queue_name} Transacciones encoladas: {queue_value}"
        notification.notify(
            title=f"Notificación de Cola: {queue_name}",
            message=message,
            timeout=10  # Duración de la notificación en segundos
        )
        print("Notificación enviada al sistema operativo.")
    except Exception as e:
        print(f"Error al enviar la notificación de Windows: {e}")

def send_telegram_notification(queue_name, queue_value):
    """Envía una notificación a un grupo de Telegram."""
    url = f"https://api.telegram.org/bot{telegram_config['token']}/sendMessage"
    message = f"⚠️ Notificación: QUEUE {queue_name} Transacciones encoladas: {queue_value}"
    
    params = {
        "chat_id": telegram_config["chat_id"],
        "text": message
    }
    
    try:
        response = requests.post(url, params=params)
        if response.status_code == 200:
            print("Notificación enviada a Telegram.")
        else:
            print(f"Error al enviar la notificación a Telegram: {response.status_code}")
    except Exception as e:
        print(f"Error al enviar la notificación a Telegram: {e}")
