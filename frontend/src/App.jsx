import { useState, useEffect } from 'react';
import './App.css';

import { BrowserRouter, Routes, Route} from 'react-router-dom';

import LoginPage from './pages/LoginPage';
import LoadingSpinner from './atoms/LoadingSpinner';
import NotLoggedPage from './pages/NotLoggedPage';
import NotFoundPage from './pages/NotFoundPage';
import Home from './pages/Home';
import useFetch from './hooks/useFetch';
// import { defineConfig, loadEnv } from 'vite';
const teste = `${import.meta.env.VITE_API_URL}/login`;
function App() {
    const [rqst, setTry] = useState(false);
    console.log("making request to url: ", `${import.meta.env.VITE_API_URL}/login`)
    console.log(rqst);
    const changeState = () => setTry(!rqst);
    const {data, error, isLoading} = useFetch(
        teste,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(
                {
                    email: "anyone@anyone.com",
                    password: "anyone"
                }
            )
        }
    );
    if (isLoading) return <h1>Loading</h1>
    if (error) return <h1>Error: {2*3}</h1>
    if (data) return <h1>Data</h1>

    console.log(fetch);
//  return <div>
//     <p> URL: {import.meta.env.VITE_API_URL}</p>
//     <button onClick={changeState}>Click me</button>
//     <BrowserRouter>
//         <Routes>
//             <Route path="/home" element={<Home/>}/>
//             <Route path="/login" element={<LoginPage />} />
//             <Route path="/loggedout" element={<NotLoggedPage/>} />
//             <Route path="*" element={<NotFoundPage/>} />
//         </Routes> 
//     </BrowserRouter>
//  </div> 
}

export default App;
