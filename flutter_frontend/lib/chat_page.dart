import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:web_socket_channel/web_socket_channel.dart';

class ChatPage extends StatefulWidget {
  final String token;

  ChatPage({required this.token});

  @override
  _ChatPageState createState() => _ChatPageState();
}

class _ChatPageState extends State<ChatPage> {
  late WebSocketChannel _webSocketChannel;
  final _controller = TextEditingController();
  final _messages = <String>[];
  

  @override
  void initState() {
    super.initState();
    _connectWebSocket();
  }

  void _connectWebSocket() {
    _webSocketChannel = WebSocketChannel.connect(
      Uri.parse('ws://127.0.0.1:8000/ws/langflow/'),
    );

    _webSocketChannel.stream.listen((data) {
      final message = jsonDecode(data);
      setState(() {
        _messages.add(message['response'] ?? 'No response');
      });
    }, onError: (error) {
      setState(() {
        _messages.add('Error: $error');
      });
    });

    // Send token for authentication
    _sendAuthenticationToken();
  }

  void _sendAuthenticationToken() {
    if (widget.token.isNotEmpty) {
      _webSocketChannel.sink.add(jsonEncode({'auth': widget.token}));
    }
  }

  void _sendMessage() {
    final message = _controller.text;
    if (message.isNotEmpty) {
      _webSocketChannel.sink.add(jsonEncode({'question': message}));
      _controller.clear();
    }
  }

  @override
  void dispose() {
    _webSocketChannel.sink.close();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Chat')),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: _messages.length,
              itemBuilder: (context, index) => ListTile(
                title: Text(_messages[index]),
              ),
            ),
          ),
          Padding(
            padding: EdgeInsets.all(8.0),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _controller,
                    decoration: InputDecoration(
                      hintText: 'Type your question',
                    ),
                  ),
                ),
                IconButton(
                  icon: Icon(Icons.send),
                  onPressed: _sendMessage,
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
