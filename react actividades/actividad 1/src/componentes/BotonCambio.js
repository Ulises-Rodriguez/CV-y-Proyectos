import React from 'react';

const BotonCambio = ({colores,setColores}) => {

  const cambio = ()=>{
    if (colores === "white") {
      setColores("red");
    } else {
      setColores("white");
    }
  }

  return (
    <>
      <button className='boton_cambio' onClick={()=> cambio()}>Boton 3</button>
    </>
  );
}

export default BotonCambio;