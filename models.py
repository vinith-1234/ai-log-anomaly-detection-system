from pydantic import BaseModel

class LogResult(BaseModel):
    filename: str
    anomaly_score: float
    risk: str
    features: list