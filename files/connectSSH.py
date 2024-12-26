import os
import paramiko
from paramiko import SSHClient
from scp import SCPClient

def download_file_from_server(remote_host, remote_port, username, key_file, remote_path, local_path):
    try:
        # Validar si la carpeta local existe
        if not os.path.exists(os.path.dirname(local_path)):
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        # Crear un cliente SSH
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Conectarse al servidor remoto usando la clave privada
        print(f"Conectando a {remote_host}:{remote_port} con clave SSH...")
        ssh.connect(
            hostname=remote_host,
            port=remote_port,
            username=username,
            key_filename=key_file  # Especificar el archivo de clave privada
        )
        
        # Crear un cliente SCP a partir de la conexión SSH
        with SCPClient(ssh.get_transport()) as scp:
            print(f"Descargando archivo desde {remote_path} a {local_path}...")
            scp.get(remote_path, local_path, preserve_times=True)  # Descargar el archivo
            
        print("Archivo descargado con éxito.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssh.close()

# Ejemplo de uso
if __name__ == "__main__":
    remote_host = "172.31.10.200"
    remote_port = 22  # Puerto SSH (por defecto es 22)
    username = "spatino"
    key_file = "C:\\Users\\HP\\.ssh\\id_rsa.pub"  # Ruta a tu clave privada
    remote_path = "/tmp/Queues.dat"
    local_path = "C:\\Users\\HP\\Desktop\\GEOCOM\\notificacionesColasIntegrador\\Queues.dat"
    
    download_file_from_server(remote_host, remote_port, username, key_file, remote_path, local_path)
