import socket
import psutil

class SystemService:
     @staticmethod
     def get_system_location() -> dict:
       "Fetches the  current local host name and Ip address. """
       hostname = socket.gethostname(hostname)
       ip address = socket.gethostname(hostname)
     return {"hostname": hostname, "ip_address": ip address}

@staticmethod

status = "Safe" if cpu_usage < 85 and memory percent is less than 85 else critical

return {
"cpu_usage_percent": cpu-usage,
"memory_usage_percent": memory.percent,
"capacity_status": status
}
