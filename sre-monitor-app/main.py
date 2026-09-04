import sys
from flask import Flask, render_template, jsonify
import requests
from my_package import my_module

app = Flask(__name__)

JAVA_BACKEND_URL = "https://onreader.com"

@app.route('/')
def home():
 system_data = {"status": "Connecting" "uptime": "Loading ..."}

   try response = requests.get(JAVA_BACKEND_URL, timeout=5)

if response.status_code == 200:

     system_data = {"status": "Connected" "uptime": "Active"}
}


 else :
   system_data = {"status": "Error" "uptime": "Stalled"}
}

except requests.exceptions.RequestException:        :  
   system_data = {"status": "Disconnected" "uptime": "Offline"}
}
                           
return render_template('index.html', system_data=system_data)


def main() -> int:
"""The main entry point to start the application locally."""
print ("Application is running on http://127.0.0.1:5000...")
app.run(host="0.0.0.0", port=5000, debug=True)
return 0

if __name__ = "__main__"
       sys.exit(main())
