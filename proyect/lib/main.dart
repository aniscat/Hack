import 'package:flutter/material.dart';
import 'api_service.dart';
import 'package:flutter_form_builder/flutter_form_builder.dart';
import 'package:form_builder_validators/form_builder_validators.dart';

class RegisterScreen extends StatefulWidget {
  @override
  _RegisterScreenState createState() => _RegisterScreenState();
}


class _RegisterScreenState extends State<RegisterScreen> {
  late Future<List<dynamic>> futureItems; //Lista de items para mandar a la base de datos
  final _formKey = GlobalKey<FormBuilderState>();
  final ApiService apiService = ApiService(baseUrl: 'http://localhost:5000/items'); //url de la conexion del servidor donde esta la API

 @override
  void initState() {
    super.initState();
    futureItems = apiService.getItems();
  }

// Construyendo el widget u tilizando la libreria Forma Builer
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Crear Nueva Cuenta'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: FormBuilder(
          key: _formKey,
          child: Column(
            children: <Widget>[
              FormBuilderTextField(
                name: 'nombre',
                decoration: InputDecoration(
                  labelText: 'Nombre',
                ),
                validator: FormBuilderValidators.compose([
                  FormBuilderValidators.required(), //Otra liberia para autentificar los datos que introduce el usuario
                  FormBuilderValidators.minLength(3),
                ]), 
              ),
              SizedBox(height: 16),
              FormBuilderTextField(
                name: 'correo',
                decoration: InputDecoration(
                  labelText: 'Correo Electrónico',
                ),
                validator: FormBuilderValidators.compose([
                  FormBuilderValidators.required(),
                  FormBuilderValidators.email(),
                ]),
              ),
              SizedBox(height: 16),
              FormBuilderTextField(
                name: 'contraseña',
                decoration: InputDecoration(
                  labelText: 'Contraseña',
                ),
                obscureText: true,
                validator: FormBuilderValidators.compose([
                  FormBuilderValidators.required(),
                  FormBuilderValidators.minLength(6),
                ]),
              ),
              SizedBox(height: 32),
              ElevatedButton(
                onPressed: () async {
                  if (_formKey.currentState?.saveAndValidate() ?? false) {
                    final formData = _formKey.currentState?.value;
                    print('Form data: $formData');
                    // Lógica para crear una cuenta
                    await apiService
                    .createItem(formData?['nombre'],formData?['correo'], formData?['contraseña']);
                        
                    setState(() {
                      futureItems = apiService.getItems();
                      print("items: $futureItems");
                    });
                  } else {
                    print('Validation failed');
                  }
                },
                child: Text('Registrar'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

void main() {
  runApp(MaterialApp(
    home: RegisterScreen(),
  ));
}
