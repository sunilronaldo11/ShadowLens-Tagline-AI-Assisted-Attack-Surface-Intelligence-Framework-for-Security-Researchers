import socket

class DNSIntel:
    def run(self, target, inventory):
        try:
            inventory.add("ip", socket.gethostbyname(target))
        except:
            inventory.add("ip", "unknown")