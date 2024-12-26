import paramiko
from paramiko import SSHClient
from scp import SCPClient

def download_file(remote_host, remote_port, username, key_file, remote_path, local_path):
    """Descarga un archivo desde un servidor remoto usando SSH y SCP."""
    try:
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=remote_host, port=remote_port, username=username, key_filename=key_file)

        with SCPClient(ssh.get_transport()) as scp:
            scp.get(remote_path, local_path, preserve_times=True)

        print(f"Archivo descargado con éxito: {local_path}")
    except Exception as e:
        print(f"Error al descargar el archivo: {e}")
    finally:
        ssh.close()
