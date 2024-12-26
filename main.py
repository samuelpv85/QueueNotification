from monitor_queues.downloader import download_file
from monitor_queues.analyzer import analyze_queues
from monitor_queues.config import remote_config, local_config
from monitor_queues.utils import ensure_directory_exists

if __name__ == "__main__":
    # Descargar el archivo
    ensure_directory_exists(local_config["local_path"])
    download_file(
        remote_host=remote_config["host"],
        remote_port=remote_config["port"],
        username=remote_config["username"],
        key_file=remote_config["key_file"],
        remote_path=remote_config["remote_path"],
        local_path=local_config["local_path"]
    )

    # Analizar el archivo descargado
    analyze_queues(local_config["local_path"])
