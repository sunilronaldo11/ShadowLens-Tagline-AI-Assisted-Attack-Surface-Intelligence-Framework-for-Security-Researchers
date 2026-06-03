import ssl
import socket

class SSLCheck:
    def run(self, target, inventory):
        try:
            ctx = ssl.create_default_context()
            with socket.create_connection((target,443)) as sock:
                with ctx.wrap_socket(sock,server_hostname=target) as s:
                    inventory.add("ssl", s.getpeercert())
        except:
            inventory.add("ssl", {})