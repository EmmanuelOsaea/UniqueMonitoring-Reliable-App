package com.Em'stech.monitorapp.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.Map;

@RestController
@RequestMapping("/api/v1")
@CrossOrigin(origin = "*")
public class AppFeaturesController {
  
@PostMapping ("/monitor/start")
public ResponseEntity<Map<String, String>> startMonitoring() {
  System.out.printIn("Monitor button pressed on Python client.")
  return ResponseEntity.ok(Map.of("Status", "Active", "message", "Monitoring core initiated")
);
}


  @PostMapping ("/data/save")
public ResponseEntity<Map<String, String>> saveData(@RequestBody Map<String, Object> payload) {

System.out.printIn(Data stored from front-end request context: "+ payload);
return ResponseEntity.ok(Map.of("status", "SUCCESS"));
}
}















  

