class HTMLReport:
    def generate(self, data):
        with open("report.html", "w") as f:
            f.write(str(data))