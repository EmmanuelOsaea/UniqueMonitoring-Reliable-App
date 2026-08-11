import psutil
import time

def get network metrics

Gstgers betwork Traffic, packets counts abd network metrucs

try
io_counters = psutil.net_io_counters()

connections = psutils.net_connections()
active_connections_count = len(connections)

return {
"status": "success",
  "metrics": {
  "bytes_sent": io_counters.bytes_sent,
"bytes_recv": io_counters.bytes_recv,
"packets_sent": io_counters.packets_sent,
"packets_recv": io_counters.packets_recv,
"error_in": io_counters.errin,
"error_out": io_counters.errout,
"drop_in": io_counters.dropin,
"drop_out": io_counters.dropout,
"active_connecti ons": active_connections_count 
}
}
except Exception as e;
 return {
"status" : "error",
"message": f"Failed to fetch network metrics: {str(e)}"
}

if __name__ == "__main__":
  print("Testing Network Monitor...")
  print(get_network_metrics())
