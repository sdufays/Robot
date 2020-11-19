
import java.net.http.HttpClient;
import java.lang.Object;

class client extends Object {
  public static void main(String[] args) {
  }
  public static void forward(){
    HttpClient client = HttpClient.newHttpClient();
    HttpRequest request = HttpRequest.newBuilder()
      .uri(URI.create("192.168.1.116:8080/fwd"))
      .build();
    client.sendAsync(request, BodyHandlers.ofString());
  }
  public static void reverse(){
    HttpClient client = HttpClient.newHttpClient();
    HttpRequest request = HttpRequest.newBuilder()
      .uri(URI.create("192.168.1.116:8080/rev"))
      .build();
    client.sendAsync(request, BodyHandlers.ofString());
  }
  public static void left(){
    HttpClient client = HttpClient.newHttpClient();
    HttpRequest request = HttpRequest.newBuilder()
      .uri(URI.create("192.168.1.116:8080/left"))
      .build();
    client.sendAsync(request, BodyHandlers.ofString());
  }
  public static void right(){
    HttpClient client = HttpClient.newHttpClient();
    HttpRequest request = HttpRequest.newBuilder()
      .uri(URI.create("192.168.1.116:8080/right"))
      .build();
    client.sendAsync(request, BodyHandlers.ofString());
  }
}