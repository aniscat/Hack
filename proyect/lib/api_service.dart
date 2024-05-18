import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  final String baseUrl;

  ApiService({required this.baseUrl});

  Future<List<dynamic>> getItems() async {
    final response = await http.get(Uri.parse('$baseUrl'));

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to load items');
    }
  }

  Future<void> createItem(String name, String email, String contrasena) async {
    final response = await http.post(
      Uri.parse('$baseUrl'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({'_id': null,'nombre': name, 'correo': email, 'contraseña': contrasena}),
    );

    if (response.statusCode != 201) {
      throw Exception('Failed to create item');
    }
  }
}
