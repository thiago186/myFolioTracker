import { useState } from 'react';

import EmailInput from '../../molecules/EmailInput';
import PasswordInput from '../../molecules/PasswordInput';
import Button from '../../atoms/Button';
import './LoginForm.css';  

function LoginForm({ onSubmit }) {
    let [email, setEmail] = useState("");
    let [password, setPassword] = useState("");

    const handleSubmit = (event) => {
        console.log("handle submit entered")
        event.preventDefault();
        console.log(email, password);
        onSubmit({ email, password });
    };

    const handleEmailChange = (event) => {
        setEmail(event.target.value);
    }

    const handlePasswordChange = (event) => {
        setPassword(event.target.value);
    }

    return (
        <form className="login-form" onSubmit={handleSubmit}>
            <h1>Login 🚀</h1>
            <div className='email-password-block'>
                <EmailInput onChange={handleEmailChange}/>
                <PasswordInput onChange={handlePasswordChange}/>
            </div>
        <Button type="submit">Login</Button>
        </form>
    );
}

export default LoginForm;
