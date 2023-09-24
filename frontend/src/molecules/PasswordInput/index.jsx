import React from 'react';
import InputField from '../../atoms/InputField';
import './PasswordInput.css';

function PasswordInput({ ...props }) {
  return (
    <div className="password-input-wrapper">
      <label htmlFor="passwordInputField">Password</label>
      <InputField 
        id="passwordInputField"
        type="password" 
        {...props}
      />
    </div>
  );
}

export default PasswordInput;
