import { useState } from 'react';

import EmailInput from '../../molecules/EmailInput';
import PasswordInput from '../../molecules/PasswordInput';
import Button from '../../atoms/Button';
import './LoginForm.css';  
import useFetch from '../../hooks/useFetch';

function LoginForm({ onLoginSuccess, onLoginFailure}) {
    const [credentials, setCredentials] = useState({ email: "", password: "" });
    const {data, error, isLoading} = useFetch();

    const handleChange = (e) => {
        const {name, value} = e.target;
        setCredentials((prev)=>({...prev, [name]: value}));
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        const {error} = await useFetch(`${import.meta.env.VITE_API_URL}/login`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(credentials)
        });

        if (error){
            onLoginFailure(error);
        } else{
            onLoginSuccess();
        }
    }


    return (
        <div>
            {error && <div className="error-alert">Invalid Credentials</div>}
            <form className="login-form" onSubmit={handleSubmit}>
            <h1>Login 🚀</h1>
            <div className='email-password-block'>
                <EmailInput onChange={handleChange}/>
                <PasswordInput onChange={handleChange}/>
            </div>
            <Button type="submit">Login</Button>
            </form>
        </div>
        
    );
}

export default LoginForm;
