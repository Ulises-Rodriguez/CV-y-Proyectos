import React from 'react';

const BotonTexto = ({setRes}) => {

  const escribir = ()=>{
    setRes("Hola todo bien?");
  }

  return (
    <>
      <button className='boton_texto' onClick={()=> escribir()}>Boton 1</button>
    </>
  );
}

export default BotonTexto;