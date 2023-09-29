import React from 'react';
import './NotFoundPage.css';

const NotFoundPage = () => {
  return (
    <div className="not-found-page">
      <h1>404</h1>
      <p>Desculpe, mas não conseguimos encontrar essa página.</p>
      <a href="/login">Faça Login</a>
    </div>
  );
};

export default NotFoundPage;
