import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_frontend/authentication.dart';

void main() {
  testWidgets('LoginPage has a username and password field and a login button', (WidgetTester tester) async {
    await tester.pumpWidget(MaterialApp(home: LoginPage()));

    expect(find.byKey(Key('username')), findsOneWidget);
    expect(find.byKey(Key('password')), findsOneWidget);
    expect(find.byKey(Key('loginButton')), findsOneWidget);
  });
}
