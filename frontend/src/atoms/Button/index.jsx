import React from 'react';
import "./Button.css";

function Button({children, onClick, type='button', ...props}) {
    return (
        <button className="btn" type={type} onClick={onClick} {...props}>
          {children}
        </button>
      );
}

export default Button;