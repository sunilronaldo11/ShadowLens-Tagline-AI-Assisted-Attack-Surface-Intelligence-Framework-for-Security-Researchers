# modules/headers.py

import requests

class Headers:
    def run(self, target, inventory):
        try:
            r = requests.get(f"https://{target}", timeout=5)
            inventory.add("headers", dict(r.headers))
        except:
            inventory.add("headers", {})