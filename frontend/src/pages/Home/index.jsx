import React from 'react';

import useFetch from '../../hooks/useFetch';
import { Navigate, useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import axios from 'axios';

function Home() {
    const navigate = useNavigate();
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const handleClick = () => {
        navigate('/login');
    }

    const validateToken = () => {
        setIsLoading(true);
        axios
        .get(
            `${import.meta.env.VITE_API_URL}/users/validate_token`, 
            {
                withCredentials: true
            }
        )
          .then((response) => {
            setIsLoading(false);
            setData(response);
          })
          .catch((error) => {
            setIsLoading(false);
            setError(error);
          });
    }

    useEffect(() => {
        console.log("inside");
        validateToken();
    }, []);

    if (error) {
        console.log(error)
        return (
            <div>
                <h1> Desculpe, mas essa página só está disponível para usuários logados</h1>
                <button onClick= {handleClick}>Ir para a página de login</button>
            </div>
        )
    } else {
        if (!isLoading){
            return (
                <div>
                    <h1>This is the home page for logged users</h1>
                </div>
            );
        }
        
    }

    
}

export default Home;
