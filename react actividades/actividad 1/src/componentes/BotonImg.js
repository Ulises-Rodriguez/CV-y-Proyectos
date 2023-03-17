import React from 'react';
import logo from "../assets/logo512.png"

const BotonImg = ({setRes}) => {
  
  const imagen = ()=>{
    setRes(<img src={logo} alt=""></img>);
  }

  return (
    <>
      <button className='boton_img' onClick={()=> imagen()}>Boton 2</button>
    </>
  );
}

export default BotonImg;