import { useState } from 'react';

import EmailInput from '../../molecules/EmailInput';
import PasswordInput from '../../molecules/PasswordInput';
import Button from '../../atoms/Button';
import './LoginForm.css';  
import useSubmit from '../../hooks/useSubmit';
import axios from 'axios';


function LoginForm({ onLoginSuccess, onLoginFailure}) {
    const [credentials, setCredentials] = useState({ email: "", password: "" });
    const [responseData, setResponseData] = useState(null);
    const [error, setError] = useState(null);
    const [isLoading, setIsLoading] = useState(false);

    const handleChange = (e) => {
        const {name, value} = e.target;
        setCredentials((prev)=>({...prev, [name]: value}));
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true);
        axios.post(`${import.meta.env.VITE_API_URL}/users/login`, credentials)
            .then((responseData) => {
                setResponseData(responseData);
                onLoginSuccess();
            })
            .catch((error) => {
                setError(error);
                onLoginFailure(error);
            }).finally(() => {
                setIsLoading(false);
            })
        
    }


    return (
        <div>
            <form className="login-form" onSubmit={handleSubmit}>
            <h1>Login 🚀</h1>
            <div className='email-password-block'>
                <EmailInput onChange={handleChange} type="email" name="email"/>
                <PasswordInput onChange={handleChange} type="password" name="password"/>
            </div>
            {error && <div className="invalid-credentials">
                Email ou senha incorretos. Por favor, tente novamente
            </div>}
            <Button type="submit" disabled={isLoading}>Login</Button>
            </form>
        </div>
        
    );
}

export default LoginForm;
