import 'package:integration_test/integration_test.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_frontend/main.dart'; // Update with your project path

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  testWidgets('login flow test', (WidgetTester tester) async {
    // Build the app and trigger a frame
    await tester.pumpWidget(MyApp());

    // Find widgets
    final usernameField = find.byKey(Key('username'));
    final passwordField = find.byKey(Key('password'));
    final loginButton = find.byKey(Key('loginButton'));

    // Interact with widgets
    await tester.enterText(usernameField, 'testuser');
    await tester.enterText(passwordField, 'password');
    await tester.tap(loginButton);

    // Wait for the widget to be updated
    await tester.pumpAndSettle();

    // Verify the login was successful
    expect(find.text('Welcome, testuser!'), findsOneWidget); // Update with actual result verification
  });
}
