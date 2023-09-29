import React from 'react';

import useFetch from '../../hooks/useFetch';
import { Navigate, useNavigate } from 'react-router-dom';
import { useEffect } from 'react';

function Home() {
    const navigate = useNavigate();
    const handleClick = () => {
        navigate('/login');
    }

    const { data, error, isLoading} = useFetch(
        `${import.meta.env.VITE_API_URL}/users/validate_token`, {withCredentials: true}
    );
    
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
