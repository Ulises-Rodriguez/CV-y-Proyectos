import React,{useState} from 'react';

const LoginOut = ({setAuth}) => {
  return (
    <div>
        <h2>LoginOut</h2>
        {setAuth(false)}
    </div>
  )
}

export default LoginOut;