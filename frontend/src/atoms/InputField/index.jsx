import "./InputField.css";

import React from 'react';
import './InputField.css';

function InputField({ type = 'text', ...props }) {
  return (
    <input 
      className="input-field"
      type={type}
      {...props}
    />
  );
}

export default InputField;
