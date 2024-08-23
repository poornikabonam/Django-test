import 'package:flutter/material.dart';
import 'package:flutter_frontend/authentication.dart';
import 'package:flutter_frontend/chat_page.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Chat',
      theme: ThemeData(primarySwatch: Colors.blue),
      initialRoute: '/',
      routes: {
        '/': (context) => LoginPage(),
        '/chat': (context) => ChatPage(
          token: ModalRoute.of(context)!.settings.arguments as String,
        ),
      },
    );
  }
}
