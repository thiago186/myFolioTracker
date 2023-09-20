export default function LoginForms(){
  return (
    <form>
      <div>
        <h1>Login Page</h1>
        <label htmlFor="userEmailLogin">Email: </label>
        <input type="email" id="userEmailLogin" />
        <label htmlFor="userPasswordLogin">Password: </label>
        <input type="password" id="userPasswordLogin"/>
      </div>
      <div>
        <button type="submit">Login</button>
      </div>
    </form>
  );
  }