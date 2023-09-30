import React, { useState, useEffect } from 'react';
import {Navigate, useNavigate} from 'react-router-dom';
import axios from 'axios';



function LogoutPage() {
    const [isLoggedOut, setIsLoggedOut] = useState(false);
    const navigate = useNavigate();
    useEffect(() => {
        axios
        .get(`${import.meta.env.VITE_API_URL}/users/logout`, {withCredentials: true})
        .then((response) =>{
            setIsLoggedOut(true);
            console.log(response)
        }
        )
        .catch((error) => {
            console.log(error);
        });
    }, []);

    const handleClick = () => {
        navigate("/login");
    };

    if (isLoggedOut){
        return (
            <div>
                <h1>Sua sessão foi encerrada com sucesso. Até logo!</h1>
                <button onClick={handleClick}>Fazer Login Novamente</button>
            </div>
            )
    }

    return null;
}


export default LogoutPage;