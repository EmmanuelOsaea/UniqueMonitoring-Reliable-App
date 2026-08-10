import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;

@Service
 public class MetricsService {

private final RestClient restClient = RestClient.create();
    return restClient.get()
    url ("http://localhost8000metrics")
   .retrieve()
   .body(String.Class);
 }
 }
