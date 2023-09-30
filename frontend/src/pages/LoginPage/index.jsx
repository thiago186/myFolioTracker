import './LoginPage.css'

import LoginForm from '../../organisms/LoginForm'
import { useNavigate } from 'react-router-dom';

function LoginPage() {
  const navigate = useNavigate();

  const handleLoginSuccess = () => {
    navigate("/home");
  }
  const handleLoginFailure = (error) => {
    console.log("Login failed", error);
  }

  return (
    <div className="LoginPage">
      <div className="login-card-container">
        <LoginForm 
          onLoginSuccess={handleLoginSuccess} 
          onLoginFailure={handleLoginFailure}
        />
      </div>
    </div>
  );

  // return (
  //   <div className="LoginPage">
  //     <div className="login-card-container">
  //     <LoginForm />
  //     </div>
  //   </div>
  // )
}

export default LoginPage;
