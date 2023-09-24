import EmailInput from '../../molecules/EmailInput';
import PasswordInput from '../../molecules/PasswordInput';
import Button from '../../atoms/Button';
import './LoginForm.css';

function LoginForm({ onSubmit }) {

  const handleSubmit = (e) => {
    console.log("handle submit entered")
    // e.preventDefault();
    onSubmit({ email, password });
    console.log(email, password)
  };

  return (
    <form className="login-form" onSubmit={handleSubmit}>
        <h1>Login</h1>
        <div className='email-password-block'>
            <EmailInput/>
            <PasswordInput/>
        </div>
      <Button type="submit">Login</Button>
    </form>
  );
}

export default LoginForm;
