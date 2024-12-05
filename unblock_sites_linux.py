import os

def unblock_sites(sites):
    """
    Desbloquea los sitios especificados eliminándolos del archivo hosts del sistema en Ubuntu.

    :param sites: Lista de sitios a desbloquear (ejemplo: ["facebook.com", "gmail.com"]).
    """
    hosts_path = "/etc/hosts"  # Ruta del archivo hosts en sistemas Linux/Ubuntu

    if not isinstance(sites, list) or not all(isinstance(site, str) for site in sites):
        print("Error: La lista de sitios debe contener solo cadenas de texto.")
        return

    try:
        print(f"Intentando desbloquear los siguientes sitios: {', '.join(sites)}")

        # Leer y filtrar el archivo hosts
        with open(hosts_path, "r+") as hosts_file:
            lines = hosts_file.readlines()
            hosts_file.seek(0)

            # Escribir solo las líneas que no contienen los sitios especificados
            for line in lines:
                if not any(site in line for site in sites):
                    hosts_file.write(line)

            # Truncar el archivo para eliminar cualquier contenido residual
            hosts_file.truncate()

        print("Sitios desbloqueados exitosamente.")
    except PermissionError:
        print("Error: No tienes permisos para modificar el archivo hosts. Ejecuta este script con 'sudo'.")
    except FileNotFoundError:
        print(f"Error: El archivo hosts no se encontró en la ruta {hosts_path}.")
    except Exception as e:
        print(f"Error inesperado al desbloquear sitios: {e}")

if __name__ == "__main__":
    # Lista de sitios a desbloquear (modificar según sea necesario)
    sitios_a_desbloquear = ["facebook.com", "gmail.com"]

    # Validación de entrada antes de ejecutar la función
    if not sitios_a_desbloquear:
        print("Error: No se especificaron sitios para desbloquear.")
    else:
        unblock_sites(sitios_a_desbloquear)
