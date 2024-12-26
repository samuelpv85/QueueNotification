import unittest
from monitor_queues.analyzer import analyze_queues

class TestAnalyzer(unittest.TestCase):
    def test_analyze_queues(self):
        # Crear un archivo temporal para pruebas
        file_content = "QUEUE.A=100\nQUEUE.B=300\n"
        with open("test_queues.dat", "w") as f:
            f.write(file_content)

        # Capturar la salida de la función
        with self.assertLogs() as log:
            analyze_queues("test_queues.dat", threshold=200)
            self.assertIn("⚠️ Notificación: La cola 'QUEUE.B' tiene un valor alto: 300", log.output)

if __name__ == "__main__":
    unittest.main()
