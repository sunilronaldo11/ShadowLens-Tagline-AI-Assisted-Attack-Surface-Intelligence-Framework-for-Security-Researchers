# modules/risk_engine.py

class RiskEngine:
    def calculate(self, data):
        score = 100

        headers = data.get("headers", {})

        if "Content-Security-Policy" not in headers:
            score -= 15

        if "Strict-Transport-Security" not in headers:
            score -= 10

        return max(score, 0)