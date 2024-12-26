import unittest
from unittest.mock import patch
from monitor_queues.notifier import send_windows_notification, send_telegram_notification

class TestNotifier(unittest.TestCase):
    @patch("monitor_queues.notifier.notification.notify")
    def test_send_windows_notification(self, mock_notify):
        queue_name = "GEOINTEGRATION.IN.XML.TRANSACTION.QUEUE"
        queue_value = 381
        send_windows_notification(queue_name, queue_value)
        mock_notify.assert_called_once_with(
            title=f"Notificación de Cola: {queue_name}",
            message=f"⚠️ Notificación: QUEUE {queue_name} Transacciones encoladas: {queue_value}",
            timeout=10
        )

    @patch("requests.post")
    def test_send_telegram_notification(self, mock_post):
        queue_name = "GEOINTEGRATION.IN.XML.TRANSACTION.QUEUE"
        queue_value = 381
        mock_post.return_value.status_code = 200
        send_telegram_notification(queue_name, queue_value)
        mock_post.assert_called_once()

if __name__ == "__main__":
    unittest.main()
