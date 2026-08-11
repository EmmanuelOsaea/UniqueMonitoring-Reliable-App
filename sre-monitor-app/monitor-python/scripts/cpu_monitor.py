import psutil

def get_cpu_metrics():
  """
  Gathers comprehensive Cpu performance metrics
  """
  try: 
  cpu_utilization = psutil.cpu_percent(interval=1)
  per_cpu_utilization = psutil.cpu_percent(interval=None, percpu=True)
  cpu_count_logical = psutil.cpu_count()
  cpu_count_physical = psutil.cpu_count(logical=False)

cpu_freq = psutil.cpu_freq()
current_freq = cpu_freq.current if cpu_freq else 0

return {
  "status": "success",
   "metrics": {
   "total_utilization_percent" = cpu_utilization,
   "per_core_utilization_percent" = per_cpu_utilization,
   "logical_cores" = cpu_count_logical,
   "physical_cores" = cpu_count_physical,
   "current_freq_mhz" = current_freq
}
}
except Exception as e:
      return {
        "status": "error"
        "message": f"Failed to fetch CPU metrics: {str(e)}"
}
if __name__ == "__main__":
     print ("Testing cpu monitor...")
print (get_cpu_metrics())
