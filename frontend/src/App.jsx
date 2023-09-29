import { useState } from 'react';
import './App.css';

import { BrowserRouter, Routes, Route} from 'react-router-dom';

import LoginPage from './pages/LoginPage';
import LoadingSpinner from './atoms/LoadingSpinner';
import NotLoggedPage from './pages/LoginPage/NotLoggedPage';
import NotFoundPage from './pages/NotFoundPage';

function App() {
 return <div>
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
