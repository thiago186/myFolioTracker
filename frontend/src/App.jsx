import { useState, useEffect } from 'react';
import './App.css';

import { BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';

import LoginPage from './pages/LoginPage';
import LoadingSpinner from './atoms/LoadingSpinner';
import NotLoggedPage from './pages/NotLoggedPage';
import NotFoundPage from './pages/NotFoundPage';
import Home from './pages/Home';
import useSubmit from './hooks/useSubmit';

// import { defineConfig, loadEnv } from 'vite';
const teste = `${import.meta.env.VITE_API_URL}/users/login`;
function App() {
    return <div>
        <p> URL: {import.meta.env.VITE_API_URL}</p>
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Navigate to="/login"/>}/>
                <Route path="/home" element={<Home/>}/>
                <Route path="/login" element={<LoginPage />} />
                <Route path="/loggedout" element={<NotLoggedPage/>} />
                <Route path="*" element={<NotFoundPage/>} />
            </Routes> 
        </BrowserRouter>
    </div> 
}

export default App;
