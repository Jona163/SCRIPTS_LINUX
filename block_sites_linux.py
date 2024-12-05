import os

def block_sites(sites):
    """
    Bloquea los sitios especificados agregándolos al archivo hosts del sistema en Ubuntu.

    :param sites: Lista de sitios a bloquear (ejemplo: ["facebook.com", "gmail.com"]).
    """
    hosts_path = "/etc/hosts"  # Ruta del archivo hosts en sistemas Linux/Ubuntu
    redirect_ip = "127.0.0.1"

    if not isinstance(sites, list) or not all(isinstance(site, str) for site in sites):
        print("Error: La lista de sitios debe contener solo cadenas de texto.")
        return

    try:
        print(f"Bloqueando los siguientes sitios: {', '.join(sites)}")

        # Leer el archivo actual
        with open(hosts_path, "r") as hosts_file:
            existing_lines = hosts_file.readlines()

        # Escribir nuevas entradas si no existen ya
        with open(hosts_path, "a") as hosts_file:
            for site in sites:
                entry = f"{redirect_ip} {site}\n"
                if entry not in existing_lines:
                    hosts_file.write(entry)
                    print(f"{site} bloqueado exitosamente.")
                else:
                    print(f"{site} ya está bloqueado.")
    except PermissionError:
        print("Error: No tienes permisos para modificar el archivo hosts. Ejecuta este script con 'sudo'.")
    except FileNotFoundError:
        print(f"Error: El archivo hosts no se encontró en la ruta {hosts_path}.")
    except Exception as e:
        print(f"Error inesperado al bloquear sitios: {e}")

if __name__ == "__main__":
    # Lista de sitios a bloquear (modificar según sea necesario)
    sitios_a_bloquear = ["facebook.com", "gmail.com"]

    # Validación de entrada antes de ejecutar la función
    if not sitios_a_bloquear:
        print("Error: No se especificaron sitios para bloquear.")
    else:
        block_sites(sitios_a_bloquear)
