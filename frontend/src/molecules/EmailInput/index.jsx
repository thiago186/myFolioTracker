import React from 'react';
import InputField from '../../atoms/InputField';
import './EmailInput.css';

function EmailInput({...props }) {
  return (
    <div className="email-input-wrapper">
      <label htmlFor="emailInputField">Email</label>
      <InputField 
        id="emailInputField"
        type="email" 
        {...props}
      />
    </div>
  );
}

export default EmailInput;
