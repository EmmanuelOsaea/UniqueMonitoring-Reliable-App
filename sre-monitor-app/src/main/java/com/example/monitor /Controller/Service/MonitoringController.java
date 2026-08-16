package com.example.monitoring;

import org.framework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestController;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMap("/api/monitoring")

public class MonitoringController{

public ResponseEntity<Map<String, String>> getSystemStatus() {
Map<String, String> statusResponse = new Hashmap<>();

statusResponse.put("status", "Connected");
statusResponse.put("uptime", "Active");
  
  return ResponseEntity.ok(statusResponse);
}
}
