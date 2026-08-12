package com.example
  import java.io.InputStream
  import java.util.properties

    public class MonitorApp {
        public static void main(String[]args) {
          MonitorApp app= new MonitorApp();
          app.loadConfig(),
           }

public void loadConfig() {
  try input stream input = get class getClass loader getResourceAsStream("config.properties")) {
    if (input == null {
      System.out.printIn("Sorry, unable to find config.properties");
      return;
    }
 Properties prop= new Properties();
    prop.load(input);
    System.out.printIn("App Name: " + prop.getProperty("app.name"));
    } catch (Exception ex) {
         ex.printStackTrace();
    }
    }
    }
