import React, { useEffect, useState } from 'react';

function WebSocketComponent({ token }) {
  const [socket, setSocket] = useState(null);
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');

  useEffect(() => {
    // Establish the WebSocket connection
    const ws = new WebSocket(`ws://localhost:8000/ws/langflow/?token=${token}`);
    setSocket(ws);

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setResponse(data.response); // Parse and set the response from the server
    };

    ws.onclose = () => {
      console.log('WebSocket connection closed');
    };

    return () => {
      ws.close(); // Clean up the WebSocket connection on component unmount
    };
  }, [token]);

  const sendQuestion = () => {
    if (socket && question) {
      socket.send(JSON.stringify({ question })); // Send the user input as 'question'
      setQuestion(''); // Clear the input field after sending
    }
  };

  return (
    <div>
      <h2>Ask a Question</h2>
      <input 
        type="text" 
        value={question} 
        onChange={(e) => setQuestion(e.target.value)} 
        placeholder="Enter your question" 
      />
      <button onClick={sendQuestion}>Send</button>
      <p>Response: {response}</p>
    </div>
  );
}

export default WebSocketComponent;
