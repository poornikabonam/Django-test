import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Register from './Register';
import Login from './Login';
import WebSocketComponent from './WebSocketPage';

function App() {
    const [token, setToken] = useState(null);
    const [showLogin, setShowLogin] = useState(false);
  
    return (
      <div>
        {!token ? (
          showLogin ? (
            <Login setToken={setToken} />
          ) : (
            <Register setToken={setToken} />
          )
        ) : (
          <WebSocketComponent token={token} />
        )}
  
        {!token && (
          <button onClick={() => setShowLogin(!showLogin)}>
            {showLogin ? 'Go to Register' : 'Go to Login'}
          </button>
        )}
      </div>
    );
  }
export default App;
