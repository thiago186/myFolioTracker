import { useState } from 'react';
import './App.css';

import { BrowserRouter, Routes, Route} from 'react-router-dom';

import LoginPage from './pages/LoginPage';
import LoadingSpinner from './atoms/LoadingSpinner';
import NotLoggedPage from './pages/NotLoggedPage';
import NotFoundPage from './pages/NotFoundPage';
// import { defineConfig, loadEnv } from 'vite';

function App() {
 return <div>
    <p> URL: {import.meta.env.VITE_API_URL}</p>
    <BrowserRouter>
        <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/loggedout" element={<NotLoggedPage/>} />
        <Route path="*" element={<NotFoundPage/>} />
        </Routes> 
    </BrowserRouter>
 </div> 
}

export default App;
