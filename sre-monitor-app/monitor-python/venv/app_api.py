# python-monitor-service/app_api.py
from fast api import FastAPI
import uvicorn
import psutil

app = FastAPI()

@app.get("/metrics")
def read_metrics():
  cpu = psutil.cpu_percent(interval=0.1)
  memory = psutil.virtual_memory.percent

  return {
    status: "healthy",
    cpu_usage: cpu,
    memory_usage: memory
  }

if __name__ == __"main"__:
uvicorn.run(app, host="12.0.0.1", port=8000)
