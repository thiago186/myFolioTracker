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

    const handleLogout = () => {
        navigate("/logout");
    }

    if (error) {
        console.log(error)
        navigate("/loggedout");
    } else {
        if (!isLoading){
            return (
                <div>
                    <h1>This is the home page for logged users</h1>
                    <button onClick={handleLogout}>Logout</button>
                </div>
            );
        }
        
    }
}

export default Home;
