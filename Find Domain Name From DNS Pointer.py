import socket

def get_domain_name(ip_address):
    try:
        domain_name = socket.gethostbyaddr(ip_address)[0]
        return domain_name
    except socket.herror:
        return None

print(get_domain_name('194.153.145.104'))
