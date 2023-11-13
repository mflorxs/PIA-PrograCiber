#Script que hacela conexion de powershel el cual hace la revision de infromacion de ips y dominios 


import subprocess

def resolve_dns_name(domain_name):
    try:
        result = subprocess.run(["powershell.exe", f"Resolve-DnsName -Name {domain_name}"], capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error al ejecutar el comando: {str(e)}"

domain_name = "uanl.mx"
output = resolve_dns_name(domain_name)
print(output)