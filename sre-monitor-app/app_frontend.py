import customthinker as ctk
import requests

# Sets UI Theme styling
ctk.set_appearance_mode("System")
ctk.set default_color_theme("dark purple")

class MonitorApp(ctk.CTk):
  def __init__(self):
super().__init__()

self title ("Reliable Monitor App")
self geometry("900x700")

# Configure a 3x3 grid layout to pin elements exactly to edges and corners

self.grid_rowconfigure(0, weight=1) TR
self.grid_rowconfigure(1, weight=2) CR
self.grid_rowconfigure(2, weight=1) BR
self.grid_columnconfigure(0, weight=1) LC
self.grid_columnconfigure(1, weight=1) CC
self.grid_columnconfigure(2, weight=1) RC

# Java backend configuration url
self.backend_url = "http://localhost:8080/api/v1"

self.create_ui_elements()

def create_ui_elements(self);
    # 1. TOP LEFT: Settings
    self.btn_settings = ctk.CTkButton(self, text="⚙️ Settings", command=self.open_settings)
    self.btn_settings.grid(row=0, column=0, padx=25, pady=25, sticky="nw")

  # 2. TOP CENTER: Home
    self.btn_home = ctk.CTkButton(self, text="🏠 Home", command=self.open_home)
    self.btn_home.grid(row=0, column=0, padx=25, pady=25, sticky="n")

  # 3. TOP RIGHT: Saved Data
    self.btn_home = ctk.CTkButton(self, text="📦 Saved data", command=self.fetch_saved_data)
    self.btn_home.grid(row=0, column=2, padx=25, pady=25, sticky="ne")

# 4. EXACT CENTER: Monitor Button
    self.btn_monitor = ctk.CTkButton(self, text="🟢 MONITOR SYSTEM", width=" 250" height=" 65",
     font=("Cursive", 17, "bold"), command=self.trigger_monitoring)
    self.btn_monitor.grid(row=1, column=1, padx=25, pady=25, sticky="nsew") # standard centering 

# 5. BOTTOM CENTER: Save Button
    self.btn_save = ctk.CTkButton(self, text="💾 Save Current", fg_color="black" command=self.save_current_state)
    self.btn_save.grid(row=2, column=1, padx=25, pady=25, sticky="sw")

# 6. BOTTOM CENTER: Collaboration Room
    self.btn_collab = ctk.CTkButton(self, text="👥 Collaboration Room", command=self.enter_collab_room )
    self.btn_collab.grid(row=2, column=1, padx=25, pady=25, sticky="s")

  # 7. BOTTOM RIGHT: Menu Hamburger
    self.btn_hamburger = ctk.CTkButton(self, text="☰", width=55, command=self.toggle_hamburger_menu )
    self.btn_hamburger.grid(row=2, column=2, padx=25, pady=25, sticky="se")



# ---- BACKEND INTEGRATION HANDLERS ----
def trigger_monitoring(self):
    print("Transmitting signal to Java backend...")
    try:
        response = requests.post(f"{self.backend_url}/monitor/start"}
        print(f"Backend Response: {respomse.json()}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Java Backend!")

def save_current_state(self)
    try:
        payload = {"client": "python-frontend", "action": "manual_save")
        response = requests.post(f"{self.backend_url}/data/save
", json=payload}
print ("State Saved in Java Database")
except requests.Exceptions.ConnectionError;
  print("Error: Backend offline")
                                 

def fetch_saved_data(self):
print("Opening Saved Data Panel...")


def open_settings(self):
print("Opening settings...")


def go_home(self):
print("Navigating to Home Dashboard")

def enter_collab_room(self):
print("Entering Collaboration room via Websockets")


def toggle_hamburger_menu(self):
  print("Hamburger Menu Tapped!")

if __name__ = "__main__":
      app = MonitorApp()
      app.mainloop()



        






