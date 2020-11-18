HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
      .uri(URI.create("http://openjdk.java.net/"))
      .build();
HttpResponse<String> response =
      client.send(request, BodyHandlers.ofString());
System.out.println(response.statusCode());
System.out.println(response.body());