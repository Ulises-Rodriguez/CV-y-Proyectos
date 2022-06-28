import React,{useState} from 'react';

const Login = ({setAuth}) => {
  return (
    <div>
        <h2>Login</h2>
        {setAuth(true)}
    </div>
  )
}

export default Login;