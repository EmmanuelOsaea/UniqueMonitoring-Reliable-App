import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MetricsController {

private final MetricsService metricsService;

public MetricsController(MetricsService metricsService) {
       this.metricsService = metricsService;
}

@GetMapping("/api/status")
public String getStatus() {
     return "UP";
}
}
