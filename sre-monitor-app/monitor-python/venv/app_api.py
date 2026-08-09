# python-monitor-service/app.py
from fast api import FastApi
import uvicorn
import psutil

app = FastAPI()

@app.get("/metrics")
def read_metrics():
