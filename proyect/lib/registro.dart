// import 'package:flutter/material.dart';
// import 'package:flutter_form_builder/flutter_form_builder.dart';
// import 'package:form_builder_validators/form_builder_validators.dart';


// class RegisterScreen extends StatefulWidget {
//   @override
//   _RegisterScreenState createState() => _RegisterScreenState();
// }

// class _RegisterScreenState extends State<RegisterScreen> {
//   final _formKey = GlobalKey<FormBuilderState>();

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: Text('Crear Nueva Cuenta'),
//       ),
//       body: Padding(
//         padding: const EdgeInsets.all(16.0),
//         child: FormBuilder(
//           key: _formKey,
//           child: Column(
//             children: <Widget>[
//               FormBuilderTextField(
//                 name: 'nombre',
//                 decoration: InputDecoration(
//                   labelText: 'Nombre',
//                 ),
//                 validator: FormBuilderValidators.compose([
//                   FormBuilderValidators.required(context),
//                   FormBuilderValidators.minLength(context, 3),
//                 ]),
//               ),
//               SizedBox(height: 16),
//               FormBuilderTextField(
//                 name: 'correo',
//                 decoration: InputDecoration(
//                   labelText: 'Correo Electrónico',
//                 ),
//                 validator: FormBuilderValidators.compose([
//                   FormBuilderValidators.required(context),
//                   FormBuilderValidators.email(context),
//                 ]),
//               ),
//               SizedBox(height: 16),
//               FormBuilderTextField(
//                 name: 'contraseña',
//                 decoration: InputDecoration(
//                   labelText: 'Contraseña',
//                 ),
//                 obscureText: true,
//                 validator: FormBuilderValidators.compose([
//                   FormBuilderValidators.required(context),
//                   FormBuilderValidators.minLength(context, 6),
//                 ]),
//               ),
//               SizedBox(height: 32),
//               ElevatedButton(
//                 onPressed: () {
//                   if (_formKey.currentState?.saveAndValidate() ?? false) {
//                     final formData = _formKey.currentState?.value;
//                     print('Form data: $formData');
//                     // Lógica para crear una cuenta
//                   } else {
//                     print('Validation failed');
//                   }
//                 },
//                 child: Text('Registrar'),
//               ),
//             ],
//           ),
//         ),
//       ),
//     );
//   }
// }

// void main() {
//   runApp(MaterialApp(
//     home: RegisterScreen(),
//   ));
// }
