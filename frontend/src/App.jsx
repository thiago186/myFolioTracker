import { useState } from 'react'
import './App.css'

import LoginPage from './pages/LoginPage'
import LoadingSpinner from './atoms/LoadingSpinner'

function App() {
 return <div>
  <LoginPage/>
  <LoadingSpinner/>
 </div> 
}

export default App;
