# core/engine.py

from modules.inventory import Inventory
from modules.dnsintel import DNSIntel
from modules.headers import Headers
from modules.sslcheck import SSLCheck
from modules.techdetect import TechDetect
from modules.risk_engine import RiskEngine

class Engine:
    def __init__(self, target):
        self.target = target
        self.inventory = Inventory()

    def run(self):
        DNSIntel().run(self.target, self.inventory)
        Headers().run(self.target, self.inventory)
        SSLCheck().run(self.target, self.inventory)
        TechDetect().run(self.target, self.inventory)

        score = RiskEngine().calculate(self.inventory.data)

        print("\n=== RESULTS ===")
        print(self.inventory.data)
        print("Risk Score:", score)