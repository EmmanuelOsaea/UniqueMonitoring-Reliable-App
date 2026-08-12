import logging
import time
try: 
   impprt psutil
except ImportError:
psutil = None


logging.basicConfig(level=logging.INFO, format ='%(asctime)s - %(levelname)s - %(message)s')

class SystemMonitorService
def __init__(self, interval=5):
self interval = interval 

def collect_metrics(self):
if not psutil: 
logging.error("psutil is not installed. Run 'pip install psutil'.")
return{}

return {
"cpu percent": psutil cpu percent ps(interval=1)
"memory_percent": psutil virtual_memory().percent,
"disk percent": psutil disk usage('/').percent

def run(self):
logging.info("Starting System Monitor Service..")
while True
metrics = self.collect_metrics()
if metrics:
logging.info(f"Collected Metrics: {metrics}")
time.sleep(self.interval)

if __name__ == "__main__":
service = SystemMonitorService()
service.run()
