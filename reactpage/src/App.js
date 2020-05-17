import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">

<div className="center-column">

    <div className="item-row">
            <span>Home Page</span>
          </div>

    <div className="item-row">
        <p><a href = "http://127.0.0.1:8000/admin/" >Admin</a></p>
          </div>

       <div className="item-row">
        <p><a href = "http://127.0.0.1:8000/albums/">Albums & Artists</a></p>
          </div>

    <div className="item-row">
        <p><a href = "http://127.0.0.1:8000/songs/">Songs</a></p>
          </div>

    </div>

    </div>

  );
}

export default App;
