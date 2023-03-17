import React from 'react';

const BotonContador = ({count,setCount}) => {

    const aumentar = ()=>{
        setCount(count + 1);
    }

  return (
    <>
        <button className='boton_contador' onClick={()=> aumentar()}>Boton 4</button>
    </>
  )
}

export default BotonContador;