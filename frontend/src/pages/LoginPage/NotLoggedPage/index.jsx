import React from "react";

import { Link } from "react-router-dom";

function NotLoggedPage() {
  return <div>
    <p>Desculpe, mas infelizmente você não está logado 😢.</p> 
    <p>Para fazer login, volte para a nossa 
        <Link to="/login">página de login</Link>
    </p>
  </div>;
}

export default NotLoggedPage;