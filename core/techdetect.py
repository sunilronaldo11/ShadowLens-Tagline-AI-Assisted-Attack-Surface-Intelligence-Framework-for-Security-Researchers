class TechDetect:
    def run(self, target, inventory):
        headers = inventory.data.get("headers", {})
        tech = []

        server = headers.get("Server")
        if server:
            tech.append(server)

        inventory.add("tech", tech)